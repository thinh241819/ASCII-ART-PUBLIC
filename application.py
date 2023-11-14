import glob
from PIL import Image
from selenium import webdriver 
from bokeh.io.export import export_png, get_screenshot_as_png


temp_name = "file://" + "out.txt"
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

driver.get("http://127.0.0.1:5500/out.html")
driver.save_screenshot("out.png")
driver.quit()

image = get_screenshot_as_png("out.html", height=100, width=100, driver=webdriver)
export_png(image, "crop.png")

# img = Image.open("/home/out.png")
# box = (1, 1, 1000, 1000)
# area = img.crop(box)no
# area.save('cropped_image.png')