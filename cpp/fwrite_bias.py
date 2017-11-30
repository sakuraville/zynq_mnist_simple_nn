def fwrite_bias(bias, wfile_name, float_b_name, fixed_wt_name, MAGNIFICATION, size):
    import datetime
    import numpy as np
    
    f = open(wfile_name, 'w')
    todaytime = datetime.datetime.today()
    f.write('// '+wfile_name+'\n')
    strdtime = todaytime.strftime("%Y/%m/%d %H:%M:%S")
    f.write('// {0} by marsee\n'.format(strdtime))
    f.write("\n")

    f.write('const float '+float_b_name+'['+str(size)+'] = {\n\t')
    for i in range(bias.shape[0]):
        f.write(str(bias[i]))
        if (i < bias.shape[0]-1):
            f.write(", ")
    f.write("\n};\n")

    f.write("\n")
    f.write('const ap_fixed<'+str(int(np.log2(MAGNIFICATION))+1)+', 1, AP_TRN_ZERO, AP_SAT> '+fixed_wt_name+'['+str(size)+'] = {\n\t')
    for i in range(bias.shape[0]):
        b_int = int(bias[i]*MAGNIFICATION+0.5)
        if (b_int > MAGNIFICATION-1):
            b_int = MAGNIFICATION-1
        elif (b_int < -MAGNIFICATION):
            b_int = -MAGNIFICATION
        f.write(str(b_int/MAGNIFICATION))
        if (i < bias.shape[0]-1):
            f.write(", ")
    f.write("\n};\n")

    f.close()

# how to use
"""
MAGNIFICATION = 2 ** (9-1)
fwrite_bias(network.params['b1'], 'af1_bias.h', 'af1_fbias', 'af1_bias', MAGNIFICATION, 50)
fwrite_bias(network.params['b2'], 'af2_bias.h', 'af2_fbias', 'af2_bias', MAGNIFICATION, 10)
"""

