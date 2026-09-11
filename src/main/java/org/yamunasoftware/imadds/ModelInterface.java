package org.yamunasoftware.imadds;

import ai.onnxruntime.OrtEnvironment;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ModelInterface {
  private static final Logger logger = LoggerFactory.getLogger(ModelInterface.class);

  public ClassificationMessage getClassification(SensorReadingKafkaMessage message) {
    return new ClassificationMessage(message, 1);
  }

  public void setupClassification() {
    String modelPath = System.getenv("IMADDS_MODEL_PATH");
      // TODO: Finish Model Interface
//    // 1. Get the global ONNX Runtime environment
//    try (OrtEnvironment env = OrtEnvironment.getEnvironment();
//         // 2. Load the model into a tracking inference session
//         OrtSession session = env.createSession(modelPath, new OrtSession.SessionOptions())) {
//
//      System.out.println("Model loaded successfully.");
//      System.out.println("Expected Input Names: " + session.getInputNames());
//
//      // 3. Define raw sample input data (match your model's expected shape)
//      // Example: A single batch with 3 feature values (1x3 tensor)
//      float[][] rawInputData = {{1.5f, 2.3f, -0.8f}};
//
//      // 4. Wrap your raw Java primitives/arrays into native OnnxTensors
//      try (OnnxTensor inputTensor = OnnxTensor.createTensor(env, rawInputData)) {
//
//        // Construct a map pairing the tensor with the exact string name expected by the model input node
//        String inputName = session.getInputNames().iterator().next();
//        Map<String, OnnxTensor> inputs = Map.of(inputName, inputTensor);
//
//        // 5. Execute inference
//        try (OrtSession.Result results = session.run(inputs)) {
//
//          // 6. Extract the output node value (get by output name or index)
//          String outputName = session.getOutputNames().iterator().next();
//          float[][] outputData = (float[][]) results.get(outputName).get().getValue();
//
//          // Print the predicted output results
//          System.out.println("Prediction Value: " + outputData[0][0]);
//        }
//      }
//
//    } catch (OrtException e) {
//      System.err.println("Error executing ONNX inference: " + e.getMessage());
//      e.printStackTrace();
//    }
  }
}