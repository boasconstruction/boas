import os
import re

dict = {}

dict[1] = "salon"
dict[2] = "restaurant"
dict[3] = "residential"
dict[4] = "retail"
dict[5] = "residential"
dict[6] = "restaurant"
dict[7] = "residential"
dict[8] = "restaurant"
dict[9] = "officelab"
dict[10] = "residential"
dict[11] = "restaurant"
dict[12] = "salon"
dict[13] = "residential"
dict[14] = "retail"
dict[15] = "officelab"
dict[16] = "restaurant"
dict[17] = "residential"
dict[18] = "retail"
dict[19] = "restaurant"
dict[20] = "residential"
dict[21] = "officelab"
dict[22] = "residential"
dict[23] = "restaurant"
dict[24] = "residential"
dict[25] = "residential"

def my_split(s):
    return filter(None, re.split(r'(\d+)', s))

str = """<li class="cbp-item %s cbp-l-grid-masonry-height1">
    <a class="cbp-caption cbp-lightbox" data-title="%s" href="assets/img/projects/all/%s">
        <div class="cbp-caption-defaultWrap">
            <img src="assets/img/projects/all/thumbs/%s" alt="">
        </div>
        <div class="cbp-caption-activeWrap">
            <div class="cbp-l-caption-alignCenter">
                <div class="cbp-l-caption-body">
                    <div class="cbp-l-caption-title">%s</div>
                </div>
            </div>
        </div>
    </a>
</li>
"""

for file in os.listdir("."):
    if file.endswith(".jpg"):
        filename = os.path.splitext(file)[0]
        # order = int("".join(itertools.takewhile(str.isdigit, "10pizzas")))
        split = my_split(filename)

        order = int(split[0])
        name = "".join(split[1:])
        category =  dict[order]

        print str % (category, name, file, file, name)

# mogrify -thumbnail 311x300^ -gravity center -extent 311x300 '*.jpg'
# mogrify -resize 1920 *.jpg
