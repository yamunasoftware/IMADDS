package org.yamunasoftware.imadds;

import java.time.Instant;

public class ClassificationMessage {
  public String deviceId;
  public String deviceType;
  public int channel;
  public float temperature;
  public float humidity;
  public float pressure;
  public long readingTimestamp;
  public long receivedTimestamp;
  public long processStartTimestamp;
  public int classification;
  public long classificationTimestamp;

  public ClassificationMessage(SensorReadingKafkaMessage reading, int classification) {
    this.deviceId = reading.deviceId;
    this.deviceType = reading.deviceType;
    this.channel = reading.channel;
    this.temperature = reading.temperature;
    this.humidity = reading.humidity;
    this.pressure = reading.pressure;
    this.readingTimestamp = reading.readingTimestamp;
    this.receivedTimestamp = reading.receivedTimestamp;
    this.processStartTimestamp = reading.processStartTimestamp;
    this.classification = classification;
    this.classificationTimestamp = Instant.now().getEpochSecond();
  }
}