from files import ImageFile
from segmentation import ContourSegmenter
from feature_extraction import SimpleFeatureExtractor
from classification import KNNClassifier
from ocr import OCR, accuracy, show_differences

segmenter = ContourSegmenter(blur_y=5, blur_x=5, block_size=11, c=10)
extractor = SimpleFeatureExtractor(feature_size=10, stretch=False)
classifier = KNNClassifier()
ocr = OCR(segmenter, extractor, classifier)

ocr.train(ImageFile('digits1'))

test_image = ImageFile('digits2')
test_chars, test_classes, test_segments = ocr.ocr(test_image, show_steps=True)

print("accuracy:", accuracy(test_image.ground.classes, test_classes))
print("OCRed text:\n", test_chars)
