# New Version:
# imageai.Prediction no longer exists, replaced by imageai.Classification
from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()
# 1/25: The executuion path

prediction = ImageClassification()
# SqueezeNet model also no longer exists, now the fastest is MobileNetV2
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

predctions, probabilities = prediction.classifyImage(os.path.join(
    exec_path, 'house.jpg'),
                                                     result_count=5)
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')

# -------------
# Old Version:
from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(
    os.path.join(execution_path,
                 "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(
    execution_path, "giraffe.jpg"),
                                                     result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
