#!/usr/bin/env bash
# Rebuild optimised WebP/AVIF assets from images/raw (ImageMagick 7 / 6 'convert').
# Replace files in images/raw with photographer shots later and re-run.
set -euo pipefail
cd "$(dirname "$0")/.."
R=images/raw; O=assets/img; T=$(mktemp -d); mkdir -p "$O"
grade="-modulate 100,96,100 -level 2%,99%"
out(){ convert "$1" -strip -quality 80 -define webp:method=6 "$O/$2.webp"; convert "$1" -strip -quality 55 "$O/$2.avif"; }
wide(){ convert "$R/$1" -resize "$3"x $grade "$T/a.png"; out "$T/a.png" "$2"; }
convert $R/img02.jpg -filter Lanczos -resize 1800x -unsharp 0x0.8+0.6+0.02 $grade $T/a.png; out $T/a.png hero-orchard
wide img22.jpg orchard-rows 1600; wide img04.jpg orchard-young 1000; wide img05.jpg orchard-tree 1000
wide img07.jpg catkins 1200; wide img03.jpg hazel-branch 1200; wide img17.jpg warehouse-hall 1100
wide img19.jpg warehouse-pallets 1600; wide img16.jpg forklift-loading 1000; wide img20.jpg forklift-pallet 1000
wide img21.jpg big-bags 1000
# Client-supplied facility photos (19.11.2026)
wide img23-branch-cluster.jpg step-cultivation 1200; wide img24-silos-hall.jpg step-processing 1400
wide img25-clean-hall.jpg processing-hall 1400; wide img26-sorting.jpg step-quality 776
wide img27-truck-bigbags.jpg truck-bigbags 900
convert $R/img24-silos-hall.jpg -filter Lanczos -resize 1800x $grade $T/a.png; out $T/a.png hero-production
tone(){ convert "$1" $grade \( +clone -fill "#FAF7F2" -colorize 100 \) -compose Multiply -composite "$T/s2.png"; out "$T/s2.png" "$2"; }
sq(){ convert "$R/$1" -gravity "$3" -crop "$4" +repage -resize 1000x1000^ -gravity center -extent 1000x1000 "$T/s.png"; tone "$T/s.png" "$2"; }
convert $R/img03.jpg -filter Lanczos -resize 1800x -unsharp 0x0.8+0.6+0.02 $grade $T/a.png; out $T/a.png hero-branch
sq img12.jpg g-natural-kernels south 896x896+0+150
sq img01.jpg p-blanched center 600x600+0+0
sq img14.jpg g-roasted-kernels south 848x848+0+180
sq img15.jpg p-chopped center 800x800+0+0
sq img08.jpg p-flour center 772x772+0+0
sq img03.jpg p-inshell east 727x727+0+0
sq img13.jpg g-natural-vacuum center 700x700+0+20
sq img10.jpg g-natural-carton south 896x896+0+150
sq img11.jpg g-natural-carton2 south 896x896+0+150
sq img18.jpg g-blanched-vacuum center 1024x1024+0+0
sq img09.jpg g-chopped-blanched center 800x800+0+0
# Client-supplied Bionut pack shots (21.11.2026)
sq img28-natural-bag.jpg p-natural north 768x768+0+240
sq img29-natural-bag2.jpg g-natural-bag2 north 768x768+0+170
sq img30-roasted-bag.jpg p-roasted north 768x768+0+150
sq img31-roasted-orchard.jpg g-roasted-orchard north 768x768+0+290
sq img32-roasted-dark.jpg g-roasted-dark north 768x768+0+150
sq img33-mixed.jpg g-mixed north 768x768+0+220
wide img34-orchard-branch.jpg orchard-branch 768
convert $R/img02.jpg -resize 1200x630^ -gravity center -extent 1200x630 -quality 82 $O/og-image.jpg
rm -rf "$T"; echo done
