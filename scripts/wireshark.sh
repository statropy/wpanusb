#!/bin/sh -x

i=0
panid=0xabcd
chan=20

ip netns delete wpan${i}
ip netns add wpan${i}
#PHYNUM=\`iwpan dev | grep -B 1 wpan${i} | sed -ne '1 s/phy#\\(\[0-9\]\\)/\\1/p'\`
PHY=`iwpan phy | grep -m1 wpan_phy | cut -d' ' -f2`
iwpan ${PHY} set netns name wpan${i}

ip netns exec wpan${i} iwpan dev wpan${i} set pan_id $panid
ip netns exec wpan${i} iwpan phy ${PHY} set channel 0 $chan
ip netns exec wpan${i} ip link add link wpan${i} name lowpan${i} type lowpan
ip netns exec wpan${i} ip link set wpan${i} up
ip netns exec wpan${i} ip link set lowpan${i} up
ip netns exec wpan${i} ip -6 addr add 2001:db8::1 dev lowpan0
ip netns exec wpan${i} wireshark -kSl -i lowpan${i} &
