"This program gives the Evaluation Metrics - Accuracy, Precision and Recall"


def accuracy(tp, tn, total):
    """
    Method to calculate accuracy
    @param tp: True Positive
    @param tn: True Negative
    @param total: Total
    @return: Calculated accuracy in float
    """
    return (tp + tn ) / total


def precision(tp, fp):
    """
    Method to calculate precision
    @param tp: True Positive
    @param fp: False Positive
    @return: Calculated precision in float
    """
    return tp / (tp + fp)


def recall(tp, fn):
    """
    Method to calculate recall
    @param tp: True Positive
    @param fn: False Negative
    @return: Calculated recall in float
    """
    return tp / (tp + fn)


def evaluation_before_augmentation(tp, tn, fp, fn):
    """
    Method to run evaluation with before augmentation values
    @param tp: True Positive
    @param tn: True Negative
    @param fp: False Positive
    @param fn: False Negative
    @return: None
    """
    total = tp + tn + fp + fn
    print("Evaluation before augmentation")
    print("Accuracy : " + str(accuracy(tp, tn, total) * 100) + " %" )
    print("Precision : " + str(precision(tp, fp) * 100) + " %")
    print("Recall : " + str(recall(tp, fn) * 100) + " %")


def evaluation_after_augmentation(tp, tn, fp, fn):
    """
    Method to run evaluation with after augmentation values
    @param tp: True Positive
    @param tn: True Negative
    @param fp: False Positive
    @param fn: False Negative
    @return: None
    """
    total = tp + tn + fp + fn
    print("Evaluation after augmentation")
    print("Accuracy : " + str(accuracy(tp, tn, total) * 100) + " %" )
    print("Precision : " + str(precision(tp, fp) * 100) + " %")
    print("Recall : " + str(recall(tp, fn) * 100) + " %")

def main():
    """
    Main driver function of the program
    @rtype: object
    """
    # The following are values calculated manually after running test on 25 images from different videos
    true_positive = 29
    true_negative = 5
    false_positive = 5
    false_negative = 6
    evaluation_before_augmentation(true_positive, true_negative, false_positive, false_negative)

    # The following are values calculated manually after running test on 25 images from different videos with
    # augmentation
    true_positive = 34
    true_negative = 3
    false_positive = 5
    false_negative = 3
    evaluation_after_augmentation(true_positive, true_negative, false_positive, false_negative)


if __name__ == '__main__':
    main()