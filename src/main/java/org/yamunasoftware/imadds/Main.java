package org.yamunasoftware.imadds;

import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.atomic.AtomicBoolean;

public class Main {
  private static final AtomicBoolean keepRunning = new AtomicBoolean(true);

  public static void main(String[] args) {
    KafkaConsumer<String, String> consumer = setupConsumer();
    String kafkaTopic = System.getenv("KAFKA_TOPIC");

    try (consumer) {
      consumer.subscribe(Collections.singletonList(kafkaTopic));
      while (keepRunning.get()) {

      }
    }
  }

  private static KafkaConsumer<String, String> setupConsumer() {
    String bootstrapServers = System.getenv("KAFKA_BOOTSTRAP_SERVERS");
    String groupId = System.getenv("KAFKA_GROUP_ID");

    Properties kafkaProps = new Properties();
    kafkaProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
    kafkaProps.put(ConsumerConfig.GROUP_ID_CONFIG, groupId);
    kafkaProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
    kafkaProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
    return new KafkaConsumer<>(kafkaProps);
  }
}