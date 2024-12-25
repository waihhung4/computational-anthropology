import cv2
import numpy as np

# def align_and_compare_images(image_path_sumerian, image_path_chinese):
#     # Load images in grayscale
#     image_sumerian = cv2.imread(image_path_sumerian, cv2.IMREAD_GRAYSCALE)
#     image_chinese = cv2.imread(image_path_chinese, cv2.IMREAD_GRAYSCALE)

#     # Initialize SIFT detector
#     sift = cv2.SIFT_create()

#     # Detect keypoints and compute descriptors
#     keypoints_sumerian, descriptors_sumerian = sift.detectAndCompute(image_sumerian, None)
#     keypoints_chinese, descriptors_chinese = sift.detectAndCompute(image_chinese, None)

#     # Set up FLANN parameters and match descriptors
#     index_params = dict(algorithm=1, trees=5) 
#     search_params = dict(checks=50)
#     flann = cv2.FlannBasedMatcher(index_params, search_params)
    
#     matches = flann.knnMatch(descriptors_sumerian, descriptors_chinese, k=2)
    

#     # # Filter matches using Lowe's ratio test
#     good_matches = [m for m,n in matches if m.distance < 0.7 * n.distance]
    
#     print(len(good_matches))

#     # src_pts = np.float32([keypoints_sumerian[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     # dst_pts = np.float32([keypoints_chinese[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

#     # # Compute homography matrix using RANSAC
#     # M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

#     # # Calculate mean Euclidean distance of good matches
#     # distances = [m.distance for m in good_matches]
#     # mean_distance = np.mean(distances)

#     # print(f'Mean Euclidean Distance: {mean_distance:.2f}')
    
#     # return M  # Return the homography matrix if needed for further processing
    
# Load the images

def align_and_compare_images(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Find keypoints and descriptors with SIFT
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

    # Create a BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw the matches
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Display the result
    cv2.imshow('Matches', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Calculate similarity score
    good_matches = [m for m in matches if m.distance < 50]  # Adjust threshold as needed
    similarity_score = len(good_matches) / len(matches) if matches else 0
    print(f'Similarity Score: {similarity_score:.2f}')


# Example usage with paths to your images
align_and_compare_images('sumerian.png', 'chinese.png')

