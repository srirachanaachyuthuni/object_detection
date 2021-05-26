# This program creates a bar graph and line chart for visualisation
import matplotlib.pyplot as plt
import numpy as np


def bar_graph():
    """
    Method to create a bar graph to show evaluation criteria - before and after augmentation.
    """
    N = 3
    before_aug = (75.56, 85.29, 82.86)
    after_aug = (82.22, 87.18, 91.89)

    ind = np.arange(N)
    width = 0.35
    plt.bar(ind, before_aug, width, label='Before Augmentation')
    plt.bar(ind + width, after_aug, width, label='After Augmentation')

    plt.ylabel('Percentage')
    plt.title('Comparison between Evaluation Criteria before nd after augmentation')

    plt.xticks(ind + width / 2, ('Accuracy', 'Precision', 'Recall'))
    plt.legend(loc='best')
    plt.show()


def line_chart():
    """
    Method to create a line chart to show the number of objects detected correctly after augmentation per image
    """
    images = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10',
              'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17', 'image18', 'image19',
              'image20', 'image21', 'image22', 'image23', 'image24', 'image25']
    true_positives_before = np.array([1,1,2,0,5,3,10,1,1,1,1,0,0,3,0,2,0,1,1,2,3,2,1,0,0])
    true_positives_after = np.array([2,1,2,1,5,3,10,1,1,1,1,0,0,4,2,4,2,2,1,2,3,2,1,0,0])
    plt.plot(images, true_positives_before, color='red', marker='o', label='Before Augmentation')
    plt.plot(images, true_positives_after, color='blue', marker='o', label='After Augmentation')
    plt.title('Comparison between objects detected before and after augmentation', fontsize=14)
    plt.xlabel('Image name', fontsize=14)
    plt.ylabel('Number of objects detected correctly', fontsize=14)
    plt.legend(loc='best')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def main():
    """
    Main driver function of the program
    @rtype: object
    """
    bar_graph()
    line_chart()


if __name__ == '__main__':
    main()





