package org.yamunasoftware.imadds;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MessageProcessor {
  private static final Logger logger = LoggerFactory.getLogger(MessageProcessor.class);

  private final String outgoingTopic;
  private final KafkaTemplate<String, ClassificationMessage> kafkaTemplate;
  private final ModelInterface modelInterface;

  public MessageProcessor(
    KafkaTemplate<String, ClassificationMessage> kafkaTemplate,
    ModelInterface modelInterface,
    @Value("OUTGOING_KAFKA_TOPIC") String outgoingTopic
  ) {
    this.kafkaTemplate = kafkaTemplate;
    this.modelInterface = modelInterface;
    this.outgoingTopic = outgoingTopic;
  }

  @KafkaListener(topics = "{INCOMING_KAFKA_TOPIC}", groupId = "{KAFKA_GROUP_ID}")
  public void consume(SensorReadingMessage incomingMessage) {
    try {
      SensorReadingKafkaMessage message = new SensorReadingKafkaMessage(incomingMessage);
      ClassificationMessage classificationMessage = modelInterface.getClassification(message);
      kafkaTemplate.send(outgoingTopic, classificationMessage);
    }

    catch (Exception e) {
      logger.error("Unexpected Classification Processing Error", e);
    }
  }
}