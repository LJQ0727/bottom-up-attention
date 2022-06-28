import logging
import numpy as np
import os
import os.path as op
import shutil
from misc import mkdir
from tsv_file import TSVFile
from tsv_file import generate_lineidx_file

#generate_lineidx_file('./metacoco/img.tsv', './metacoco/img.lineidx')
# generate_lineidx_file('./metacoco/hw.tsv', './metacoco/hw.lineidx')

# generate_lineidx_file('ori_oscar_5000/pred.coco_caption.test.beam5.max20.odlabels.tsv', 'ori_oscar_5000/pred.coco_caption.test.beam5.max20.odlabels.lineidx')
# generate_lineidx_file('ana_oscar_3280/pred.oscar_3280.test.beam5.max20.odlabels.tsv', 'ana_oscar_3280/pred.oscar_3280.test.beam5.max20.odlabels.lineidx')
# generate_lineidx_file('./oscar_3280/test.label.tsv', './oscar_3280/test.label.lineidx')

# tsv1 = TSVFile('./test.feature.tsv')
# tsv2 = TSVFile('./test.label.tsv')

# dir = 'inserted_result_same_0_feature'
# dir = 'inserted_result_same_bar1_feature'
# dir = '1000_test_bg_images_feature'
# dir = 'zzq_1000_bg_feature'
# dir = 'zzq_last_suspicious879_feature'
# dir = 'inserted_result_same_bar3_feature'
# dir = 'order_final_bg_test_feature'
# dir = 'inserted_result_same11_22_feature'
# generate_lineidx_file(os.path.join(dir,'test.feature.tsv'), os.path.join(dir,'test.feature.lineidx'))
# generate_lineidx_file(os.path.join(dir,'test.label.tsv'), os.path.join(dir,'test.label.lineidx'))

# generate_lineidx_file( 'zzq_37_bg_feature/test.feature.tsv', 'zzq_37_bg_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_37_bg_feature/test.label.tsv', 'zzq_37_bg_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_37_test_0_feature/test.feature.tsv', 'zzq_37_test_0_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_37_test_0_feature/test.label.tsv', 'zzq_37_test_0_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_37_test_bar1_feature/test.feature.tsv', 'zzq_37_test_bar1_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_37_test_bar1_feature/test.label.tsv', 'zzq_37_test_bar1_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_37_test_bar2_feature/test.feature.tsv', 'zzq_37_test_bar2_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_37_test_bar2_feature/test.label.tsv', 'zzq_37_test_bar2_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_37_test_bar3_feature/test.feature.tsv', 'zzq_37_test_bar3_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_37_test_bar3_feature/test.label.tsv', 'zzq_37_test_bar3_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_87_bg_images_feature/test.feature.tsv', 'zzq_87_bg_images_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_87_bg_images_feature/test.label.tsv', 'zzq_87_bg_images_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_87_final_result_test_0_feature/test.feature.tsv', 'zzq_87_final_result_test_0_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_87_final_result_test_0_feature/test.label.tsv', 'zzq_87_final_result_test_0_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_87_final_result_test_bar1_feature/test.feature.tsv', 'zzq_87_final_result_test_bar1_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_87_final_result_test_bar1_feature/test.label.tsv', 'zzq_87_final_result_test_bar1_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_87_final_result_test_bar2_feature/test.feature.tsv', 'zzq_87_final_result_test_bar2_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_87_final_result_test_bar2_feature/test.label.tsv', 'zzq_87_final_result_test_bar2_feature/test.label.lineidx' )

# generate_lineidx_file( 'zzq_87_final_result_test_bar3_feature/test.feature.tsv', 'zzq_87_final_result_test_bar3_feature/test.feature.lineidx' )
# generate_lineidx_file( 'zzq_87_final_result_test_bar3_feature/test.label.tsv', 'zzq_87_final_result_test_bar3_feature/test.label.lineidx' )

# generate_lineidx_file( 'baopo_bg_images_feature/test.feature.tsv', 'baopo_bg_images_feature/test.feature.lineidx' )
# generate_lineidx_file( 'baopo_bg_images_feature/test.label.tsv', 'baopo_bg_images_feature/test.label.lineidx' )

# generate_lineidx_file( 'baopo_final_result_test_0_feature/test.feature.tsv', 'baopo_final_result_test_0_feature/test.feature.lineidx' )
# generate_lineidx_file( 'baopo_final_result_test_0_feature/test.label.tsv', 'baopo_final_result_test_0_feature/test.label.lineidx' )

# generate_lineidx_file( 'baopo_final_result_test_bar1_feature/test.feature.tsv', 'baopo_final_result_test_bar1_feature/test.feature.lineidx' )
# generate_lineidx_file( 'baopo_final_result_test_bar1_feature/test.label.tsv', 'baopo_final_result_test_bar1_feature/test.label.lineidx' )

# generate_lineidx_file( 'baopo_final_result_test_bar2_feature/test.feature.tsv', 'baopo_final_result_test_bar2_feature/test.feature.lineidx' )
# generate_lineidx_file( 'baopo_final_result_test_bar2_feature/test.label.tsv', 'baopo_final_result_test_bar2_feature/test.label.lineidx' )

# generate_lineidx_file( 'deeptest_blur_feature/test.feature.tsv', 'deeptest_blur_feature/test.feature.lineidx' )
# generate_lineidx_file( 'deeptest_blur_feature/test.label.tsv', 'deeptest_blur_feature/test.label.lineidx' )

# generate_lineidx_file( 'deeptest_brightness_feature/test.feature.tsv', 'deeptest_brightness_feature/test.feature.lineidx' )
# generate_lineidx_file( 'deeptest_brightness_feature/test.label.tsv', 'deeptest_brightness_feature/test.label.lineidx' )

# generate_lineidx_file( 'deeptest_contrast_feature/test.feature.tsv', 'deeptest_contrast_feature/test.feature.lineidx' )
# generate_lineidx_file( 'deeptest_contrast_feature/test.label.tsv', 'deeptest_contrast_feature/test.label.lineidx' )

# generate_lineidx_file( 'deeptest_shear_feature/test.feature.tsv', 'deeptest_shear_feature/test.feature.lineidx' )
# generate_lineidx_file( 'deeptest_shear_feature/test.label.tsv', 'deeptest_shear_feature/test.label.lineidx' )

generate_lineidx_file( 'metaicpp_results_50_feature/test.feature.tsv', 'metaicpp_results_50_feature/test.feature.lineidx' )
generate_lineidx_file( 'metaicpp_results_50_feature/test.label.tsv', 'metaicpp_results_50_feature/test.label.lineidx' )
