package org.yamunasoftware.imadds;

import org.apache.kafka.clients.consumer.*;
import java.time.Duration;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;

public class Main {
  private static String topic = "imadds";
  private static final AtomicBoolean keepRunning = new AtomicBoolean(true);

  public static void main(String[] args) {
    KafkaConsumer<String, String> consumer = setupConsumer();

    try (consumer) {
      consumer.subscribe(Collections.singletonList(topic));
      while (keepRunning.get()) {
        ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
        for (ConsumerRecord<String, String> record : records) {
          Map<String, Object> row = new HashMap<>();

        }
      }
    }
  }

  private static KafkaConsumer<String, String> setupConsumer() {
    Properties kafkaProps = new Properties();
    kafkaProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    kafkaProps.put(ConsumerConfig.GROUP_ID_CONFIG, "snowflake-group");
    kafkaProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
    kafkaProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
    return new KafkaConsumer<>(kafkaProps);
  }
}