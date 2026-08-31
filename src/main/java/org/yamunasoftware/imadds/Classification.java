package org.yamunasoftware.imadds;

public class Classification {
  public String deviceId;
  public String deviceType;
  public int channel;
  public float temperature;
  public float humidity;
  public float pressure;
  public long readingTimestamp;
  public int classification;
  public long  classificationTimestamp;

  public Classification(
      String deviceId, String deviceType, int channel, float temperature, float humidity,
      float pressure, long readingTimestamp, int classification, long  classificationTimestamp) {
    this.deviceId = deviceId;
    this.deviceType = deviceType;
    this.channel = channel;
    this.temperature = temperature;
    this.humidity = humidity;
    this.pressure = pressure;
    this.readingTimestamp = readingTimestamp;
    this.classification = classification;
    this.classificationTimestamp = classificationTimestamp;
  }
}