/* loldht.c */
// Testing program for simulated sensor output
// Author: Stefan Lengauer
// Date: 2016-01-01
#include <stdio.h>

int main(void)
{
  char sample_output[] = "Raspberry Pi wiringPi DHT22 reader\nwww.lolware.net\nData not good, skip\nHumidity = 44.50 % Temperature = 21.50 *C \n";
  printf("%s", sample_output);

  return 0;
}