
class BaseImagingBackend:

    def impose_text(base_image, text, pos, font_path=None,
                     color="black", size=12):
        pass

    def impose_image(base_image, top_image, box, center=True):
        pass

    def save_image(img, path, fmt=None):
        pass

    def fit_and_position(img, box, center=True):
        pass

    def get_image_palette(img, maxcolors=100):
        pass

    def boxsize(box):
        w = box[2] - box[0]
        h = box[3] - box[1]
        return (w, h)
