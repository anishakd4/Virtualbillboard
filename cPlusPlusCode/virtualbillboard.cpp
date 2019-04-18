#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/calib3d.hpp>
#include<iostream>

using namespace std;
using namespace cv;

int main(){

    //Read the virtual billboard and banner images
    Mat virtualbillboard = imread("../assets/virtualbillboard.jpg");
    Mat banner = imread("../assets/virtual_billboard_banner.jpg");

    //Creating a copy of virtual billboard image to work on
    Mat virtualbillboardClone = virtualbillboard.clone();

    vector<Point2f> pts_billboard, pts_banner;

    //four corners of the banner in the virtual billboard image to be replaced
    pts_billboard.push_back(Point2f(91, 56));
    pts_billboard.push_back(Point2f(224, 79));
    pts_billboard.push_back(Point2f(225, 158));
    pts_billboard.push_back(Point2f(89, 147));

    //four corners of our banner
    pts_banner.push_back(Point2f(0, 0));
    pts_banner.push_back(Point2f(banner.size().width - 1, 0));
    pts_banner.push_back(Point2f(banner.size().width - 1, banner.size().height - 1));
    pts_banner.push_back(Point2f(0, banner.size().height - 1));

    Mat result;

    //Calculate homography from banner to billboard
    Mat homographyMat = findHomography(pts_banner, pts_billboard);

    //warp banner on to billboard image
    warpPerspective(banner, result, homographyMat, virtualbillboardClone.size());

    //Black out the polygonal banner area in the virtual billboard image
    Point dstPoints[4];
    for(int i=0 ;i <4; i++){
        dstPoints[i] = pts_billboard[i];
    }
    fillConvexPoly(virtualbillboardClone, dstPoints, 4, Scalar(0), CV_AA);

    //Add warped banner image to the virtual billboard image
    virtualbillboardClone = virtualbillboardClone + result;

    //create windows to show images
    namedWindow("virtualbillboard", WINDOW_NORMAL);
    namedWindow("banner", WINDOW_NORMAL);
    namedWindow("result1", WINDOW_NORMAL);
    namedWindow("result2", WINDOW_NORMAL);

    //display images
    imshow("virtualbillboard", virtualbillboard);
    imshow("banner", banner);
    imshow("result1", result);
    imshow("result2", virtualbillboardClone);

    //Press esc to exit the program
    waitKey(0);

    //Close all the opened windows
    destroyAllWindows();
    
    return 0;
}