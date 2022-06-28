cd bottom-up-attention

# Generate tsv files
python2 tools/tsv_gen.py --gpu 0 --cfg experiments/cfgs/faster_rcnn_end2end_resnet.yml --def models/vg/ResNet-101/faster_rcnn_end2end_final/test.prototxt \
 --out feature/custom.feature.tsv --net data/faster_rcnn_models/resnet101_faster_rcnn_final.caffemodel --split custom
chown jiaqi .  -R