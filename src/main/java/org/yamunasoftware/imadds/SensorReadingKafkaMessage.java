package org.yamunasoftware.imadds;

import java.time.Instant;

public class SensorReadingKafkaMessage {
  public String deviceId;
  public String deviceType;
  public int channel;
  public float temperature;
  public float humidity;
  public float pressure;
  public long readingTimestamp;
  public long receivedTimestamp;
  public long processStartTimestamp;

  public SensorReadingKafkaMessage(SensorReadingMessage message) {
    this.deviceId = message.deviceId;
    this.deviceType = message.deviceType;
    this.channel = message.channel;
    this.temperature = message.temperature;
    this.humidity = message.humidity;
    this.pressure = message.pressure;
    this.readingTimestamp = message.readingTimestamp;
    this.receivedTimestamp = message.receivedTimestamp;
    this.processStartTimestamp = Instant.now().getEpochSecond();
  }
}