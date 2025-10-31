# KD4MT: A Survey of Knowledge Distillation for Machine Translation

This is the list of the papers surveyed in the manuscript "KD4MT: A Survey of Knowledge Distillation for Machine Translation."

In this repository, we provide the full list of surveyed papers as well as the database that we have compiled for our analysis, paired with our glossary of key terms in KD4MT. You can find the database [here](data/database.tsv).

  - [Abstract](#abstract)
  - [Paper List](#paper-list)
    - [Methods](#methods)
    - [Multilingual MT](#multilingual-mt)
    - [Low-resource MT](#low-resource-mt)
    - [Domain Adaptation](#domain-adaptation)
    - [Time-Sensitive Applications](#time-sensitive-applications)
    - [Other](#other)
  - [Glossary](#glossary)
  - [Citation](#citation)


## Abstract

Large-scale Machine Translation (MT) systems pose a challenge in terms of their environmental impact and accessibility. 
One method to produce more efficient machine translation models is Knowledge Distillation (KD). 
This survey comprehensively explores the application of KD in the domain of MT. 

## Paper List

### Methods

Chen, Yen-Chun, Zhe Gan, Yu Cheng, Jingzhou Liu, and Jingjing Liu. 2020. Distilling knowledge learned in BERT for text generation. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pages 7893–7905, Association for Computational Linguistics, Online.

Finkelstein, Mara and Markus Freitag. 2024. Mbr and qe finetuning: Training-time distillation of the best and most expensive decoding methods. *The Twelfth International Conference on Learning Representations*.

Jafari, Aref, Mehdi Rezagholizadeh, Pranav Sharma, and Ali Ghodsi. 2021. Annealing knowledge distillation. In *Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume*, pages 2493–2504, Association for Computational Linguistics, Online.

Jin, Heegon, Seonil Son, Jemin Park, Youngseok Kim, Hyungjong Noh, and Yeonsoo Lee. 2024. Align-to-distill: Trainable attention alignment for knowledge distillation in neural machine translation. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, pages 722–732.

Kim, Yoon and Alexander M. Rush. 2016. Sequence-level knowledge distillation. In *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing*, pages 1317–1327, Association for Computational Linguistics, Austin, Texas.

Lee, Dongkyu, Zhiliang Tian, Yingxiu Zhao, Ka Chun Cheung, and Nevin Zhang. 2022a. Hard gate knowledge distillation – leverage calibration for robust and reliable language model. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 9793–9803, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates.

Lee, Dongkyu, Zhiliang Tian, Yingxiu Zhao, Ka Chun Cheung, and Nevin Zhang. 2022b. Hard gate knowledge distillation – leverage calibration for robust and reliable language model. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 9793–9803.

Li, Jiahuan, Shanbo Cheng, Shujian Huang, and Jiajun Chen. 2024. Mt-patcher: Selective and extendable knowledge distillation from large language models for machine translation.

Liang, Xiaobo, Lijun Wu, Juntao Li, Tao Qin, Min Zhang, and Tie-Yan Liu. 2022. Multi-teacher distillation with single model for neural machine translation. *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 30:992–1002.

Lin, Alexander, Jeremy Wohlwend, Howard Chen, and Tao Lei. 2020. Autoregressive knowledge distillation through imitation learning. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 6121–6133, Association for Computational Linguistics, Online.

Lin, Ye, Yanyang Li, Ziyang Wang, Bei Li, Quan Du, Tong Xiao, and Jingbo Zhu. 2021. Weight distillation: Transferring the knowledge in neural network parameters. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 2076–2088, Association for Computational Linguistics, Online.

Miao, Zhongjian, Wen Zhang, Jinsong Su, Xiang Li, Jian Luan, Yidong Chen, Bin Wang, and Min Zhang. 2023. Exploring all-in-one knowledge distillation framework for neural machine translation. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 2929–2940, Association for Computational Linguistics, Singapore.

Setiawan, Hendra. 2024. Accurate knowledge distillation via n-best reranking. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 1330–1345, Association for Computational Linguistics, Mexico City, Mexico.

Song, Yuncheng, Liang Ding, Changtong Zan, and Shujian Huang. 2025. Self-evolution knowledge distillation for LLM-based machine translation. In *Proceedings of the 31st International Conference on Computational Linguistics*, pages 10298–10308, Association for Computational Linguistics, Abu Dhabi, UAE.

Wang, Fusheng, Jianhao Yan, Fandong Meng, and Jie Zhou. 2021. Selective knowledge distillation for neural machine translation. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 6456–6466, Association for Computational Linguistics, Online.

Wang, Jun, Eleftheria Briakou, Hamid Dadkhahi, Rishabh Agarwal, Colin Cherry, and Trevor Cohn. 2024. Don’t throw away data: Better sequence knowledge distillation.

Wen, Yuqiao, Zichao Li, Wenyu Du, and Lili Mou. 2023. f-divergence minimization for sequence-level knowledge distillation. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 10817–10834, Association for Computational Linguistics, Toronto, Canada.

Weng, Rongxiang, Heng Yu, Shujian Huang, Shanbo Cheng, and Weihua Luo. 2020. Acquiring knowledge from pre-trained model to neural machine translation. *Proceedings of the AAAI Conference on Artificial Intelligence*, 34(05):9266–9273.

Wu, Junhong, Yang Zhao, Yangyifan Xu, Bing Liu, and Chengqing Zong. 2025. Boosting LLM translation skills without general ability loss via rationale distillation. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 12217–12236, Association for Computational Linguistics, Vienna, Austria.

Wu, Yimeng, Peyman Passban, Mehdi Rezagholizadeh, and Qun Liu. 2020. Why skip if you can combine: A simple knowledge distillation technique for intermediate layers. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1016–1021, Association for Computational Linguistics, Online.

Xu, Hongfei, Zhuofei Liang, Qiuhui Liu, and Lingling Mu. 2025. A self-distillation recipe for neural machine translation. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 5050–5064, Association for Computational Linguistics, Vienna, Austria.

Yang, Jiacheng, Mingxuan Wang, Hao Zhou, Chengqi Zhao, Weinan Zhang, Yong Yu, and Lei Li. 2020. Towards making the most of BERT in neural machine translation. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 34, pages 9378–9385.

Zhang, Dakun, Josep Crego, and Jean Senellart. 2018. Analyzing knowledge distillation in neural machine translation. In *Proceedings of the 15th International Conference on Spoken Language Translation*, pages 23–30, International Conference on Spoken Language Translation, Brussels.

Zhang, Songming, Yunlong Liang, Shuaibo Wang, Yufeng Chen, Wenjuan Han, Jian Liu, and Jinan Xu. 2023. Towards understanding and improving knowledge distillation for neural machine translation. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 8062–8079, Association for Computational Linguistics, Toronto, Canada.

Zouhar, Vilém. 2021. Sampling and filtering of neural machine translation distillation data. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Student Research Workshop*, pages 1–8, Association for Computational Linguistics, Online.

### Multilingual MT

Bapna, Ankur, Isaac Caswell, Julia Kreutzer, Orhan Firat, Daan van Esch, Aditya Siddhant, Mengmeng Niu, Pallavi Baljekar, Xavier Garcia, Wolfgang Macherey, et al. 2022. Building machine translation systems for the next thousand languages.

Do, Heejin and Gary Geunbae Lee. 2023. Target-oriented knowledge distillation with language-family-based grouping for multilingual NMT. *ACM Transactions on Asian and Low-Resource Language Information Processing*, 22(2).

Gala, Jay, Pranjal A. Chitale, A. K. Raghavan, Varun Gumma, Sumanth Doddapaneni, Janki Atul Nawale, Anupama Sujatha, Ratish Puduppully, Vivek Raghavan, Pratyush Kumar, et al. 2023. IndicTrans2: Towards high-quality and accessible machine translation models for all 22 scheduled Indian languages. *Transactions on Machine Learning Research*.

Mohammadshahi, Alireza, Vassilina Nikoulina, Alexandre Bérard, Caroline Brun, James Henderson, and Laurent Besacier. 2022. Small-100: Introducing shallow multilingual machine translation model for low-resource languages. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 8348–8359.

NLLB Team. 2024. Scaling neural machine translation to 200 languages. *Nature*, 630(8018):841–846.

Tan, Xu, Yi Ren, Di He, Tao Qin, Zhou Zhao, and Tie-Yan Liu. 2019. Multilingual neural machine translation with knowledge distillation.

Yu, Zhengzhe, Daimeng Wei, Zongyao Li, Hengchao Shang, Xiaoyu Chen, Zhanglin Wu, Jiaxin Guo, Minghan Wang, Lizhi Lei, Min Zhang, Hao Yang, and Ying Qin. 2021. HW-TSC’s participation in the WMT 2021 large-scale multilingual translation task. In *Proceedings of the Sixth Conference on Machine Translation*, pages 456–463, Association for Computational Linguistics, Online.

Zhang, Yuanchi, Yile Wang, Zijun Liu, Shuo Wang, Xiaolong Wang, Peng Li, Maosong Sun, and Yang Liu. 2024. Enhancing multilingual capabilities of large language models through self-distillation from resource-rich languages.

### Low-resource MT

Baziotis, Christos, Ivan Titov, Alexandra Birch, and Barry Haddow. 2021. Exploring unsupervised pretraining objectives for machine translation. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*, pages 2956–2971, Association for Computational Linguistics, Online.

Chang, Chen-Chi, Yu-Hsun Lin, Yun-Hsiang Hsu, and I-Hsin Fan. 2025. Integrating hybrid AI approaches for enhanced translation in minority languages. *Applied Sciences*, 15(16).

Chen, Yun, Yang Liu, Yong Cheng, and Victor O. K. Li. 2017. A teacher-student framework for zero-resource neural machine translation. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1925–1935.

Dabre, Raj and Atsushi Fujita. 2020. Combining sequence distillation and transfer learning for efficient low-resource neural machine translation models. In *Proceedings of the Fifth Conference on Machine Translation*, pages 492–502, Association for Computational Linguistics, Online.

De Gibert, Ona, Joseph Attieh, Teemu Vahtola, Mikko Aulamo, Zihao Li, Raúl Vázquez, Tiancheng Hu, and Jörg Tiedemann. 2025. Scaling low-resource MT via synthetic data generation with LLMs.

De Gibert, Ona, Mikko Aulamo, Yves Scherrer, and Jörg Tiedemann. 2024. Hybrid distillation from RBMT and NMT: Helsinki-NLP’s submission to the shared task on translation into low-resource languages of Spain. In *Proceedings of the Ninth Conference on Machine Translation*, pages 908–917, Association for Computational Linguistics, Miami, Florida, USA.

De Gibert, Ona, Raúl Vázquez, Mikko Aulamo, Yves Scherrer, Sami Virpioja, and Jörg Tiedemann. 2023. Four approaches to low-resource multilingual NMT: The Helsinki submission to the AmericasNLP 2023 shared task. In *Proceedings of the Workshop on Natural Language Processing for Indigenous Languages of the Americas (AmericasNLP)*, pages 177–191, Association for Computational Linguistics, Toronto, Canada.

Diddee, Harshita, Sandipan Dandapat, Monojit Choudhury, Tanuja Ganu, and Kalika Bali. 2022. Too brittle to touch: Comparing the stability of quantization and distillation towards developing low-resource MT models. In *Proceedings of the Seventh Conference on Machine Translation (WMT)*, pages 870–885, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates (Hybrid).

Elmadani, Khalid N. and Jan Buys. 2024. Neural machine translation between low-resource languages with synthetic pivoting. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, pages 12144–12158.

Feng, Xiaocheng, Xinwei Geng, Baohang Li, Bing Qin, et al. 2023. Towards higher Pareto frontier in multilingual machine translation. In *The 61st Annual Meeting of the Association for Computational Linguistics*.

Galiano-Jiménez, Aarón, Juan Antonio Pérez-Ortiz, Felipe Sánchez-Martínez, and Víctor M. Sánchez-Cartagena. 2025a. Beyond the mode: Sequence-level distillation of multilingual translation models for low-resource language pairs. In *Findings of the Association for Computational Linguistics: NAACL 2025*, pages 6661–6676, Association for Computational Linguistics, Albuquerque, New Mexico.

Galiano-Jiménez, Aarón, Juan Antonio Pérez-Ortiz, Felipe Sánchez-Martínez, and Víctor M. Sánchez-Cartagena. 2025b. Fluent vs. non-fluent data augmentation in knowledge distillation for machine translation for low-resource languages.

Galiano-Jiménez, Aarón, Felipe Sánchez-Martínez, Víctor M. Sánchez-Cartagena, and Juan Antonio Pérez-Ortiz. 2023. Exploiting large pre-trained models for low-resource neural machine translation. In *Proceedings of the 24th Annual Conference of the European Association for Machine Translation*, pages 59–68.

Gumma, Varun, Raj Dabre, and Pratyush Kumar. 2023. An empirical study of leveraging knowledge distillation for compressing multilingual neural machine translation models. In *Proceedings of the 24th Annual Conference of the European Association for Machine Translation*, pages 103–114.

He, Tianyu, Jiale Chen, Xu Tan, and Tao Qin. 2019. Language graph distillation for low-resource machine translation.

Oh, Seokjin, Su Ah Lee, and Woohwan Jung. 2023. Data augmentation for neural machine translation using generative language model.

Saleh, Fahimeh, Wray Buntine, and Gholamreza Haffari. 2020. Collective wisdom: Improving low-resource neural machine translation using adaptive knowledge distillation. In *Proceedings of the 28th International Conference on Computational Linguistics*, pages 3413–3421, International Committee on Computational Linguistics, Barcelona, Spain (Online).

Saleh, Fahimeh, Wray Buntine, Gholamreza Haffari, and Lan Du. 2021. Multilingual neural machine translation: Can linguistic hierarchies help? In *Findings of the Association for Computational Linguistics: EMNLP 2021*, pages 1313–1330, Association for Computational Linguistics, Punta Cana, Dominican Republic.

Sun, Yanming, Xuebo Liu, Derek F. Wong, Yuchu Lin, Bei Li, Runzhe Zhan, Lidia S. Chao, and Min Zhang. 2024. Understanding and improving low-resource neural machine translation with shallow features. In *CCF International Conference on Natural Language Processing and Chinese Computing*, pages 227–239, Springer.

Yang, Jian, Yuwei Yin, Shuming Ma, Dongdong Zhang, Shuangzhi Wu, Hongcheng Guo, Zhoujun Li, and Furu Wei. 2022. UM4: Unified multilingual multiple teacher-student model for zero-resource neural machine translation. In *Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence, IJCAI-2022*, International Joint Conferences on Artificial Intelligence Organization.

Yang, Wayne and Garrett Nicolai. 2023. Neural machine translation data generation and augmentation using ChatGPT. *arXiv preprint* arXiv:2307.05779.

Zhang, Guanghua, Hua Liu, Junjun Guo, and Tianyu Guo. 2024. Distilling BERT knowledge into seq2seq with regularized mixup for low-resource neural machine translation. *Expert Systems with Applications*, page 125314.

Zhang, Jiarui, Heyan Huang, Yue Hu, Ping Guo, and Yuqiang Xie. 2023. Importance-based neuron selective distillation for interference mitigation in multilingual neural machine translation. In *International Conference on Knowledge Science, Engineering and Management*, pages 140–150, Springer.

Zhang, Xinlu, Xiao Li, Yating Yang, and Rui Dong. 2020. Improving low-resource neural machine translation with teacher-free knowledge distillation. *IEEE Access*, 8:206638–206645.

### Domain Adaptation

Currey, Anna, Prashant Mathur, and Georgiana Dinu. 2020. Distilling multiple domains for neural machine translation. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 4500–4511, Association for Computational Linguistics, Online.

Gordon, Mitchell and Kevin Duh. 2020. Distill, adapt, distill: Training small, in-domain models for neural machine translation. In *Proceedings of the Fourth Workshop on Neural Generation and Translation*, pages 110–118, Association for Computational Linguistics, Online.

Gu, Shuhao, Yang Feng, and Wanying Xie. 2021. Pruning-then-expanding model for domain adaptation of neural machine translation. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 3942–3952, Association for Computational Linguistics, Online.

Klimaszewski, Mateusz, Zeno Belligoli, Satendra Kumar, and Emmanouil Stergiadis. 2023. Gated adapters for multi-domain neural machine translation. In *ECAI 2023*. IOS Press, pages 1264–1271.

Liang, Yunlong, Fandong Meng, Jiaan Wang, Jinan Xu, Yufeng Chen, and Jie Zhou. 2024. Continual learning with semi-supervised contrastive distillation for incremental neural machine translation. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 10914–10928, Association for Computational Linguistics, Bangkok, Thailand.

Liu, Yupeng, Lei Zhang, and Yanan Zhang. 2022. Neural machine translation transfer model based on mutual domain guidance. *IEEE Access*, 10:101595–101608.

Man, Zhibo, Yujie Zhang, Yuanmeng Chen, Yufeng Chen, and Jinan Xu. 2025. CCKA: Continual cross-domain knowledge adaptation for multi-domain machine translation. *IEEE Transactions on Audio, Speech and Language Processing*.

Mghabbar, Idriss and Pirashanth Ratnamogan. 2020. Building a multi-domain neural machine translation model using knowledge distillation. In *ECAI 2020*. IOS Press, pages 2116–2123.

Zeng, Jiali, Yang Liu, Jinsong Su, Yubing Ge, Yaojie Lu, Yongjing Yin, and Jiebo Luo. 2019. Iterative dual domain adaptation for neural machine translation. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 845–855, Association for Computational Linguistics, Hong Kong, China.

Zhao, Yang, Junnan Zhu, Lu Xiang, Jiajun Zhang, Yu Zhou, Feifei Zhai, and Chengqing Zong. 2022. Life-long learning for multilingual neural machine translation with knowledge distillation.

### Time-Sensitive Applications

Deng, Hexuan, Liang Ding, Xuebo Liu, Meishan Zhang, Dacheng Tao, and Min Zhang. 2023. Improving simultaneous machine translation with monolingual data. In *Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence*, pages 12728–12736.

Ding, Liang, Longyue Wang, Siyou Liu, Weihua Luo, and Kaifu Zhang. 2025. Widening the bottleneck of lexical choice for non-autoregressive translation. *Computer Speech & Language*, 92:101765.

Ding, Liang, Longyue Wang, Xuebo Liu, Derek F. Wong, Dacheng Tao, and Zhaopeng Tu. 2021a. Rejuvenating low-frequency words: Making the most of parallel data in non-autoregressive translation. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 3431–3441.

Ding, Liang, Longyue Wang, Xuebo Liu, Derek F. Wong, Dacheng Tao, and Zhaopeng Tu. 2021b. Understanding and improving lexical choice in non-autoregressive translation. In *International Conference on Learning Representations*.

Feng, Yang, Shuhao Gu, Dengji Guo, Zhengxin Yang, and Chenze Shao. 2021. Guiding teacher forcing with seer forcing for neural machine translation. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 2862–2872, Association for Computational Linguistics, Online.

Guo, Jiaxin, Minghan Wang, Daimeng Wei, Hengchao Shang, Yuxia Wang, Zongyao Li, Zhengzhe Yu, Zhanglin Wu, Yimeng Chen, Chang Su, et al. 2021. Self-distillation mixup training for non-autoregressive neural machine translation.

Liu, Min, Yu Bao, Chengqi Zhao, and Shujian Huang. 2023. Selective knowledge distillation for non-autoregressive neural machine translation. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 37, pages 13246–13254.

Nguyen, Xuan-Phi, Shafiq Joty, Kui Wu, and Ai Ti Aw. 2020. Data diversification: A simple strategy for neural machine translation. In *Advances in Neural Information Processing Systems*, volume 33, pages 10018–10029, Curran Associates, Inc.

Sen, Sukanta, Rico Sennrich, Biao Zhang, and Barry Haddow. 2023. Self-training reduces flicker in retranslation-based simultaneous translation. In *Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics*, pages 3734–3744, Association for Computational Linguistics, Dubrovnik, Croatia.

Shao, Chenze, Xuanfu Wu, and Yang Feng. 2022. One reference is not enough: Diverse distillation with reference selection for non-autoregressive translation. In *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 3779–3791.

Wang, Shushu, Jing Wu, Kai Fan, Wei Luo, Jun Xiao, and Zhongqiang Huang. 2023. Better simultaneous translation with monotonic knowledge distillation. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 2334–2349, Association for Computational Linguistics, Toronto, Canada.

Yu, Donglei, Xiaomian Kang, Yuchen Liu, Feifei Zhai, Nanchang Cheng, Yu Zhou, and Chengqing Zong. 2025. Investigating hallucinations in simultaneous machine translation: Knowledge distillation solution and components analysis. In *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 7116–7131, Association for Computational Linguistics, Albuquerque, New Mexico.

Zhang, Biao, Deyi Xiong, Jinsong Su, and Jiebo Luo. 2019. Future-aware knowledge distillation for neural machine translation. *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 27(12):2278–2287.

Zhang, Shaolei, Yang Feng, and Liangyou Li. 2021. Future-guided incremental transformer for simultaneous translation. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 35, pages 14428–14436.

Zhou, Chulun, Fandong Meng, Jie Zhou, Min Zhang, Hongji Wang, and Jinsong Su. 2022. Confidence based bidirectional global context aware training framework for neural machine translation. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 2878–2889, Association for Computational Linguistics, Dublin, Ireland.

Zhou, Jiawei and Phillip Keung. 2020. Improving non-autoregressive neural machine translation with monolingual data. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pages 1893–1898.

Zhuang, Yimeng and Mei Tu. 2023. Pretrained bidirectional distillation for machine translation. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1132–1145, Association for Computational Linguistics, Toronto, Canada.

### Other

Dankers, Verna and Vikas Raunak. 2025. Memorization inheritance in sequence-level knowledge distillation for neural machine translation. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*, pages 760–774, Association for Computational Linguistics, Vienna, Austria.

Gordon, Mitchell A. and Kevin Duh. 2019. Explaining sequence-level knowledge distillation as data-augmentation for neural machine translation.

Halder, Deepon, Thanmay Jayakumar, and Raj Dabre. 2025. Cycledistill: Bootstrapping machine translation using LLMs with cyclical distillation.

Huang, Yichong, Xiaocheng Feng, Xinwei Geng, and Bing Qin. 2022. Unifying the convergences in multilingual neural machine translation. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 6822–6835, Association for Computational Linguistics, Abu Dhabi, United Arab Emirates.

Li, Bei, Ziyang Wang, Hui Liu, Quan Du, Tong Xiao, Chunliang Zhang, and Jingbo Zhu. 2020. Learning light-weight translation models from deep transformer. In *AAAI Conference on Artificial Intelligence*.

Ren, Yi, Jinglin Liu, Xu Tan, Zhou Zhao, Sheng Zhao, and Tie-Yan Liu. 2020. A study of non-autoregressive model for sequence generation. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pages 149–159, Association for Computational Linguistics, Online.

Renduchintala, Adithya, Denise Diaz, Kenneth Heafield, Xian Li, and Mona Diab. 2021. Gender bias amplification during speed-quality optimization in neural machine translation. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)*, pages 99–109, Association for Computational Linguistics, Online.

Roy, Aniruddha, Pretam Ray, Ayush Maheshwari, Sudeshna Sarkar, and Pawan Goyal. 2024. Enhancing low-resource NMT with a multilingual encoder and knowledge distillation: A case study. In *Proceedings of the Seventh Workshop on Technologies for Machine Translation of Low-Resource Languages (LoResMT 2024)*, pages 64–73, Association for Computational Linguistics, Bangkok, Thailand.

Song, Yewei, Saad Ezzini, Jacques Klein, Tegawende Bissyande, Clément Lefebvre, and Anne Goujon. 2023. Letz translate: Low-resource machine translation for Luxembourgish. In *2023 5th International Conference on Natural Language Processing (ICNLP)*, pages 165–170, IEEE.

Vamvas, Jannis and Rico Sennrich. 2021. Contrastive conditioning for assessing disambiguation in MT: A case study of distilled bias. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 10246–10265, Association for Computational Linguistics, Online and Punta Cana, Dominican Republic.

Velayuthan, Menan, Nisansa De Silva, and Surangika Ranathunga. 2025. Encoder-aware sequence-level knowledge distillation for low-resource neural machine translation. In *Proceedings of the Eighth Workshop on Technologies for Machine Translation of Low-Resource Languages (LoResMT 2025)*, pages 161–170, Association for Computational Linguistics, Albuquerque, New Mexico, U.S.A.

Wei, Hao-Ran, Shujian Huang, Ran Wang, Xin-yu Dai, and Jiajun Chen. 2019. Online distilling from checkpoints for neural machine translation. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 1932–1941, Association for Computational Linguistics, Minneapolis, Minnesota.

Xu, Weijia, Shuming Ma, Dongdong Zhang, and Marine Carpuat. 2021. How does distilled data complexity impact the quality and confidence of non-autoregressive machine translation? In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*, pages 4392–4400.

Zhang, Yuanchi, Peng Li, Maosong Sun, and Yang Liu. 2023. Continual knowledge distillation for neural machine translation. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 7978–7996, Association for Computational Linguistics, Toronto, Canada.

Zhou, Chunting, Jiatao Gu, and Graham Neubig. 2020. Understanding knowledge distillation in non-autoregressive machine translation. In *International Conference on Learning Representations*.

## Glossary

We list key terms along with definitions. Page numbers indicate the first occurrence in the text.

**Adaptive KD**
Word-level KD with multiple teachers where each teacher’s weight is softmax-normalized from its negative perplexity on the data; introduced by *Saleh, Buntine, and Haffari (2020)*.

**Annealing Distillation**
Distillation where the temperature of the teacher’s output is progressively lowered (*Jafari et al. 2021*). (p. 9)

**Back-Distillation**
After distilling a student, use that student to further improve the teacher; introduced by *Tan et al. (2019a)*.

**Capacity Curse**
A larger/stronger teacher does not necessarily yield a stronger student. (p. 12)

**Capacity Gap**
Performance drop caused by size mismatch, where a smaller student lacks parameters to fit data as accurately as a larger teacher. (p. 11)

**Complementary KD**
Multiple teachers trained on data subsets unseen by the student; the student distills via Word-KD and teachers are reset from the student each epoch; proposed by *Shao and Feng (2022)*, used by *Roy et al. (2024)*.

**Data Diversification**
As introduced by *Nguyen et al. (2020)*, it consists of generating data via forward and back translation and training on the concatenation of the original and the newly created synthetic data. (p. 18)

**Feature-based KD**
Distillation from intermediate representations of the teacher (hidden states / feature maps). (p. 6)

**Multilinguality Curse**
Increasing the number of languages can hinder performance due to limited capacity (*Conneau et al. 2020*). (p. 13)

**Mutual Distillation**
Two or more models are trained simultaneously, each acting as teacher and student (*Feng et al. 2023*). (p. 11)

**Response-based KD**
Distillation from the teacher’s final predictions: token-level (Word-KD) or sentence-level (Seq-KD). (p. 6)

**Selective Distillation**
Word-KD applied conditionally (e.g., only when the teacher outperforms the student); used by *Tan et al. (2019b); Wang et al. (2021); Zhang et al. (2023a)*. (p. 24)

**Self-Distillation**
A model distills knowledge from itself, treating the student as the teacher. (p. 10)

**Sequence-Level Interpolation**
Seq-KD where the teacher proposes multiple candidates and the one closest to the reference is kept; *Kim and Rush (2016)*. (p. 10)

**Sequence-Level KD**
Distillation from the teacher’s output translation to the student; *Kim and Rush (2016)*. Also called **hard** or **offline** distillation. (p. 6)

**Top-K Distillation**
Distillation using only the teacher’s top-K probabilities instead of the full distribution; *Tan et al. (2019b)*.

**Word-Level KD**
Distillation from the teacher’s token probability distribution to the student; *Kim and Rush (2016)*. Also called **soft** or **online** distillation. (p. 6)

## Citation

Coming soon!