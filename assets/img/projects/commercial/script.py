import os

str = """<li class="cbp-item commercial cbp-l-grid-masonry-height1">
    <a class="cbp-caption cbp-lightbox" data-title="%s" href="assets/img/projects/commercial/%s">
        <div class="cbp-caption-defaultWrap">
            <img src="assets/img/projects/commercial/thumbs/%s" alt="">
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
        name = os.path.splitext(file)[0]
        print str % (name, file, file, name)

# print str
