package org.yamunasoftware.imadds;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.Collections;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtSession;

public class ModelInterface {
  private static final Logger logger = LoggerFactory.getLogger(ModelInterface.class);

  public ClassificationMessage getClassification(SensorReadingKafkaMessage message) {
    String modelPath = System.getenv("IMADDS_MODEL_PATH");

    try (OrtEnvironment env = OrtEnvironment.getEnvironment()) {
      try (OrtSession session = env.createSession(modelPath, new OrtSession.SessionOptions());) {
        float[][] features = new float[][]{{message.temperature, message.pressure, message.humidity}};
        String inputName = session.getInputNames().iterator().next();

        try (OnnxTensor inputTensor = OnnxTensor.createTensor(env, features)) {
          try (OrtSession.Result results = session.run(Collections.singletonMap(inputName, inputTensor))) {
            String outputName = session.getOutputNames().iterator().next();
            float[][] outputData = (float[][]) results.get(outputName).get().getValue();


          }
        }
      }
    }

    catch (Exception e) {
      logger.error(e.getMessage());
    }
    return null;
  }
}