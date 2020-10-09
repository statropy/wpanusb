#!/bin/sh

PHY=`iwpan phy | grep -m1 wpan_phy | cut -d' ' -f2`

INSTANCE=${1:-1}
CHAN=${2:-20}
PAN=${3:-0xabcd}
IP_ADDR=2001:db8::$INSTANCE/64
SHORT_ADDR=0xbee$INSTANCE
echo 'Using phy' $PHY 'channel' $CHAN 'PAN ID' $PAN
echo 'IP:' $IP_ADDR 'Short:' $SHORT_ADDR

iwpan dev wpan0 set pan_id $PAN
iwpan dev wpan0 set short_addr $INSTANCE
iwpan phy $PHY set channel 0 $CHAN
ip link add link wpan0 name lowpan0 type lowpan
ip link set wpan0 up
ip link set lowpan0 up
ip -6 addr add $IP_ADDR dev lowpan0
