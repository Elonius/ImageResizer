# import tensorflow as tf
from skimage import data
import imagehash
import numpy as np
import os
import sys
from PIL import Image
from matplotlib import pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

originalFolder = "coffee_beans"
attackFolder = "C:\\Users\\shawn\\Downloads\\"
attackImg = "attackimgTank.jpeg"
resizedFolder = "resizedSamples\\"
newSize = [256, 256]

sess = tf.Session()
with sess.as_default():
    image_decoded = tf.image.decode_jpeg(
                tf.io.read_file(attackFolder + attackImg), channels=3)
    pieces = attackImg.split('.')
    imgName = pieces[0]
    fileExt = pieces[1]
    
    for i in range(5, 301):
        size = [i, i]

        # BILINEAR
        actual_resize_bilinear = tf.image.resize_images(
            image_decoded, size=size, method=tf.image.ResizeMethod.BILINEAR)
        enc = tf.image.encode_jpeg(
            tf.cast(actual_resize_bilinear, tf.uint8))
        newName = imgName + "_BILINEAR_" + str(size) + "." + fileExt
        imgFileResized = os.path.join(resizedFolder, newName)
        fwrite2 = tf.io.write_file(tf.constant(imgFileResized), enc)
        sess.run(fwrite2)
        # bilinearHash = imagehash.average_hash(Image.open(imgFileResized))
        # print('BILINEAR:', bilinearHash)

        # NN
        resize_nearest_neighbor = tf.image.resize_images(
            image_decoded, size=size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
        enc = tf.image.encode_jpeg(resize_nearest_neighbor)
        newName = imgName + "_NEAREST_" + str(size) + "." + fileExt
        imgFileResized = os.path.join(resizedFolder, newName)
        fwrite3 = tf.io.write_file(tf.constant(imgFileResized), enc)
        sess.run(fwrite3)
        # nnHash = imagehash.average_hash(Image.open(imgFileResized))
        # print('NN:', nnHash)

        # BICUBIC
        actual_resize_bicubic = tf.image.resize_images(
            image_decoded, size=size, method=tf.image.ResizeMethod.BICUBIC)
        enc = tf.image.encode_jpeg(
            tf.cast(actual_resize_bicubic, tf.uint8))
        newName = imgName + "_BICUBIC_" + str(size) + "." + fileExt
        imgFileResized = os.path.join(resizedFolder, newName)
        fwrite4 = tf.io.write_file(tf.constant(imgFileResized), enc)
        sess.run(fwrite4)
        # bicubicHash = imagehash.average_hash(Image.open(imgFileResized))
        # print('BICUBIC:', bicubicHash)

        # AREA
        actual_resize_area = tf.image.resize_images(
            image_decoded, size=size, method=tf.image.ResizeMethod.AREA)
        enc = tf.image.encode_jpeg(tf.cast(actual_resize_area, tf.uint8))
        newName = imgName + "_AREA_" + str(size) + "." + fileExt
        imgFileResized = os.path.join(resizedFolder, newName)
        fwrite5 = tf.io.write_file(tf.constant(imgFileResized), enc)
        sess.run(fwrite5)
        # areaHash = imagehash.average_hash(Image.open(imgFileResized))
        # print('AREA:', areaHash)




    # for imageName in os.listdir(originalFolder):
    #     """
    #     Testing hashes for the original/attacker coffee picture
    #     """
    #     # originalImg = Image.open('C:\\Users\\shawn\\Downloads\\coffee.png')
    #     # attackImg = Image.open('C:\\Users\\shawn\\Downloads\\attackimg.png')
    #     # origHash = imagehash.whash(originalImg)
    #     # print('ORIG:', origHash)
    #     # attackHash = imagehash.whash(attackImg)
    #     # print('ATTACK:', attackHash)

    #     # print(
    #     #     f'Difference between Original & Attack:\t{origHash - attackHash} ->\t{((origHash - attackHash)/len(origHash.hash)**2)*100}%')

    #     # Shows histogram
    #     # originalImg = np.array(originalImg)
    #     # attackImg = np.array(attackImg)
    #     # histogram = plt.hist(originalImg.ravel(), bins=8)
    #     # histogram2 = plt.hist(attackImg.ravel(), bins=8)
    #     # plt.show()
    #     # break

    #     imgFileOrig = os.path.join(originalFolder, imageName)

    #     pieces = imageName.split('.')

    #     if len(pieces) == 2:
    #         imgName = pieces[0]
    #         fileExt = pieces[1]

    #         image_decoded = tf.image.decode_jpeg(
    #             tf.io.read_file(imgFileOrig), channels=3)
    #         print('IMAGE NAME:', imageName)

    #         # ORIG
    #         enc = tf.image.encode_jpeg(image_decoded)
    #         newName = imgName + "_ORIG." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite1 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite1)
    #         origHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('ORIG:', origHash)

    #         # BILINEAR
    #         actual_resize_bilinear = tf.image.resize_images(
    #             image_decoded, size=newSize, method=tf.image.ResizeMethod.BILINEAR)
    #         enc = tf.image.encode_jpeg(
    #             tf.cast(actual_resize_bilinear, tf.uint8))
    #         newName = imgName + "_BILINEAR." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite2 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite2)
    #         bilinearHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('BILINEAR:', bilinearHash)

    #         # NN
    #         resize_nearest_neighbor = tf.image.resize_images(
    #             image_decoded, size=newSize, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    #         enc = tf.image.encode_jpeg(resize_nearest_neighbor)
    #         newName = imgName + "_NEAREST." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite3 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite3)
    #         nnHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('NN:', nnHash)

    #         # BICUBIC
    #         actual_resize_bicubic = tf.image.resize_images(
    #             image_decoded, size=newSize, method=tf.image.ResizeMethod.BICUBIC)
    #         enc = tf.image.encode_jpeg(
    #             tf.cast(actual_resize_bicubic, tf.uint8))
    #         newName = imgName + "_BICUBIC." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite4 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite4)
    #         bicubicHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('BICUBIC:', bicubicHash)

    #         # AREA
    #         actual_resize_area = tf.image.resize_images(
    #             image_decoded, size=newSize, method=tf.image.ResizeMethod.AREA)
    #         enc = tf.image.encode_jpeg(tf.cast(actual_resize_area, tf.uint8))
    #         newName = imgName + "_AREA." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite5 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite5)
    #         areaHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('AREA:', areaHash)

    #         # CROP/PAD
    #         actual_resize_image_with_crop_or_pad = tf.image.resize_image_with_crop_or_pad(
    #             image_decoded, target_height=newSize[0], target_width=newSize[1])
    #         enc = tf.image.encode_jpeg(
    #             tf.cast(actual_resize_image_with_crop_or_pad, tf.uint8))
    #         newName = imgName + "_CROP-PAD." + fileExt
    #         imgFileResized = os.path.join(resizedFolder, newName)
    #         fwrite6 = tf.io.write_file(tf.constant(imgFileResized), enc)
    #         sess.run(fwrite6)
    #         cropHash = imagehash.average_hash(Image.open(imgFileResized))
    #         print('CROP/PAD:', cropHash)

    #         # Differences from original image
    #         print(
    #             f'Difference between Original & Bilinear:\t{origHash - bilinearHash} ->\t{((origHash - bilinearHash)/len(origHash.hash)**2)*100}%')
    #         print(
    #             f'Difference between Original & NN:\t{origHash - nnHash} ->\t{((origHash - nnHash)/len(origHash.hash)**2)*100}%')
    #         print(
    #             f'Difference between Original & Bicubic:\t{origHash - bicubicHash} ->\t{((origHash - bicubicHash)/len(origHash.hash)**2)*100}%')
    #         print(
    #             f'Difference between Original & Area:\t{origHash - areaHash} ->\t{((origHash - areaHash)/len(origHash.hash)**2)*100}%')
    #         print(
    #             f'Difference between Original & Crop/Pad:\t{origHash - cropHash} ->\t{((origHash - cropHash)/len(origHash.hash)**2)*100}%')
    #         break
    #     else:
    #         continue
