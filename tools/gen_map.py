#!/usr/bin/env python3
"""Generate a Robinson-projected world map (SVG path data) from world-atlas TopoJSON.

Output: tools/data/map.json  -> {"viewBox": "...", "land": "<path d>", "countries": {id: d}, "points": {...}}
Run once; build.py inlines the result into the pages.
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "data", "countries-110m.json")
OUT = os.path.join(HERE, "data", "map.json")

# Robinson projection table (lat 0..90 step 5): X, Y
ROB = [
    (1.0000, 0.0000), (0.9986, 0.0620), (0.9954, 0.1240), (0.9900, 0.1860), (0.9822, 0.2480),
    (0.9730, 0.3100), (0.9600, 0.3720), (0.9427, 0.4340), (0.9216, 0.4958), (0.8962, 0.5571),
    (0.8679, 0.6176), (0.8350, 0.6769), (0.7986, 0.7346), (0.7597, 0.7903), (0.7186, 0.8435),
    (0.6732, 0.8936), (0.6213, 0.9394), (0.5722, 0.9761), (0.5322, 1.0000),
]
W = 1000.0
LAT_MIN, LAT_MAX = -56.0, 84.0


def robinson(lon, lat):
    a = abs(lat) / 5.0
    i = min(int(a), 17)
    f = a - i
    x0, y0 = ROB[i]
    x1, y1 = ROB[i + 1]
    X = x0 + (x1 - x0) * f
    Y = y0 + (y1 - y0) * f
    x = 0.8487 * X * math.radians(lon)
    y = 1.3523 * Y * (1 if lat >= 0 else -1)
    return x, y


# scale so that lon -180..180 maps to 0..W
XMAX = 0.8487 * math.pi
S = W / (2 * XMAX)
_, YTOP = robinson(0, LAT_MAX)
_, YBOT = robinson(0, LAT_MIN)
H = (YTOP - YBOT) * S


def proj(lon, lat):
    lat = max(LAT_MIN, min(LAT_MAX, lat))
    x, y = robinson(lon, lat)
    return (x + XMAX) * S, (YTOP - y) * S


def main():
    topo = json.load(open(SRC))
    sc = topo["transform"]["scale"]
    tr = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        arcs.append(pts)

    def ring(idx_list):
        pts = []
        for i in idx_list:
            a = arcs[i] if i >= 0 else arcs[~i][::-1]
            pts.extend(a if not pts else a[1:])
        return pts

    def ring_to_d(pts):
        segs, cur, prev = [], [], None
        for lon, lat in pts:
            if prev is not None and abs(lon - prev) > 180:
                segs.append(cur)
                cur = []
            cur.append(proj(lon, lat))
            prev = lon
        segs.append(cur)
        out = []
        for s in segs:
            if len(s) < 2:
                continue
            simp = [s[0]]
            for p in s[1:]:
                if abs(p[0] - simp[-1][0]) + abs(p[1] - simp[-1][1]) > 0.6:
                    simp.append(p)
            if len(simp) < 3:
                continue
            out.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in simp) + "Z")
        return "".join(out)

    countries = {}
    for g in topo["objects"]["countries"]["geometries"]:
        name = g["properties"]["name"]
        if name == "Antarctica":
            continue
        polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]] if g["type"] == "Polygon" else []
        d = "".join(ring_to_d(ring(r)) for poly in polys for r in poly)
        countries[g.get("id") or name] = {"name": name, "d": d}

    # Marker points (lon, lat): Gabala origin + market hubs
    pts = {
        "AZ": (47.85, 40.98),   # Gabala
        "DE": (10.0, 51.0),
        "IT": (12.5, 42.8),
        "TR": (34.0, 39.2),
        "CA": (-79.4, 43.7),    # Toronto region
        "RU": (37.6, 55.75),    # Moscow
        "EG": (31.2, 30.0),     # Cairo
        "IN": (77.2, 23.5),
    }
    points = {k: [round(c, 1) for c in proj(*v)] for k, v in pts.items()}
    json.dump({"w": W, "h": round(H, 1), "countries": countries, "points": points}, open(OUT, "w"))
    print("wrote", OUT, "h=", round(H, 1), "countries:", len(countries), "bytes:", os.path.getsize(OUT))


if __name__ == "__main__":
    main()
