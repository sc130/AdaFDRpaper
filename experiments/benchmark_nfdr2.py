## system settings 
import matplotlib
matplotlib.use('Agg')
import logging
import os
import sys
import argparse

## nfdr2
import nfdr2.data_loader as dl
import nfdr2.method as md
import time
import matplotlib.pyplot as plt

def main(args):    
    use_cv = True
    n_itr = 1500
    opt = args.opt
    fname = args.file
    
    if opt=='airway':
        output_folder = os.path.realpath('..') + '/results/result_airway'
    elif opt=='2DGM':
        output_folder = os.path.realpath('..') + '/results/result_2DGM'
    elif opt=='5DGM':
        output_folder = os.path.realpath('..') + '/results/result_5DGM'
    elif opt=='GTEx_full':
        output_folder = os.path.realpath('..') + '/results/result_GTEx_full'
    elif opt=='ukbb':
        output_folder = os.path.realpath('..') + '/results/result_ukbb_%s'%fname
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        filelist = [ f for f in os.listdir(output_folder)]        
        for f in filelist:
            os.remove(os.path.join(output_folder, f))

    logging.basicConfig(level=logging.INFO,format='%(module)s:: %(message)s',\
                        filename=output_folder+'/result.log', filemode='w')
    logger = logging.getLogger()
    
    ## set up some parameters 
    log_transform = False
    h = None
    cate_name={}
    alpha=0.1
    
    ## load the data: move to data_loader
    if opt=='airway':
        p,x = dl.load_airway(verbose=True)
        n_full = p.shape[0]
    elif opt=='2DGM':
        p,h,x=dl.load_2DGM(verbose=True)
        n_full = p.shape[0]        
    elif opt=='5DGM':
        p,h,x = dl.load_5DGM(verbose=True)
        n_full = p.shape[0]
    elif opt=='GTEx_full':
        p,x,n_full,cate_name = dl.load_GTEx_full(verbose=True)
    elif opt=='ukbb':
        file = '/data/martin/NeuralFDR/ukbb_data/'+fname+'.csv'
        p,x,n_full,cate_name = dl.load_common_dataset(filename=file, n=4071752)
        log_transform = True
        
    logger.info('## %s'%opt)
    logger.info('# all hypothesis: %d'%n_full)
    logger.info('# filtered hypothesis: %d'%x.shape[0])
    for i in range(5):
        logger.info('# p=%s, x=%s'%(str(p[i]),str(x[i])))
    logger.info('')
    

    ## report the baseline   
    n_rej,t_rej=md.bh(p,alpha=alpha,n_full=n_full,verbose=False)
    logger.info('## BH, n_rej=%d, t_rej=%0.5f'%(n_rej,t_rej))
    n_rej,t_rej,pi0_hat=md.storey_bh(p,alpha=alpha,n_full=n_full,verbose=False)
    logger.info('## SBH, n_rej=%d, t_rej=%0.5f'%(n_rej,t_rej))
    
    ## feature explore function
    md.feature_explore(p,x,alpha=alpha,n_full=n_full,vis_dim=None,cate_name=cate_name,\
                       output_folder=output_folder,h=h,log_transform=log_transform)
    
    ## run the algorithm
    start_time = time.time()
    
    #x = md.feature_preprocess(x,p) 
    if use_cv:
        n_rej,t,_=md.method_hs(p,x,5,alpha=alpha,h=h,n_full=n_full,n_itr=n_itr,verbose=True,\
                                output_folder=output_folder,random_state=0)
        logger.info('## nfdr2, n_rej1=%d, n_rej2=%d, n_rej_total=%d'%(n_rej[0],n_rej[1],n_rej[0]+n_rej[1]))    
    else:
        n_rej,t,_=md.method_single_fold(p,x,5,alpha=alpha,n_full=n_full,h=h,n_itr=n_itr,verbose=True,\
                             output_folder=output_folder,if_preprocess=True)
        logger.info('## nfdr2, n_rej=%d'%(n_rej))
    # compare to h.
    #if h is not None:
        #    tol_rej = np.sum(p<t)
        #    false_rej = np.sum((p<t)*(h==0))            
        #    #logger.info('## Testing summary (ground truth) ##')
        #    #logger.info('# D=%d, FD=%d, FDP=%0.3f'%(tol_rej,false_rej,false_rej/tol_rej))
    logger.info('## Total time: %0.1fs'%(time.time()-start_time))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NeuralFDR2 multiple hypothesis testing')
    parser.add_argument('--opt', type=str, required=True)
    parser.add_argument('--file', type=str, required = True)
    args = parser.parse_args()
    main(args)