package org.yamunasoftware.imadds;

public class SensorReadingMessage {
  public String deviceId;
  public String deviceType;
  public int channel;
  public float temperature;
  public float humidity;
  public float pressure;
  public long readingTimestamp;
  public long receivedTimestamp;
}