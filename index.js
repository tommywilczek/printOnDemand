function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function waitToDownload() {
    console.log("sleeping...");
    await sleep(2000);
    console.log("done sleeping...");

  }

function saveBase64AsFile(base64, fileName) {

    var link = document.createElement("a");

    link.setAttribute("href", base64);
    link.setAttribute("download", fileName);
    link.click();
}

function generateDictOfPatterns(patternDict) {
    var colorBrewerList = {
        "Blues": "Blues",
        "Greens": "Greens",
        "Greys": "Greys",
        "Oranges": "Oranges",
        "Purples": "Purples",
        "Reds": "Reds",
        "Blue-Green": "BuGn",
        "Blue-Purple": "BuPu",
        "Green-Blue": "GnBu",
        "Orange-Red": "OrRd",
        "Purple-Blue-Green": "PuBuGn",
        "Purple-Blue": "PuBu",
        "Purple-Red": "PuRd",
        "Red-Purple": "RdPu",
        "Yellow-Green-Blue": "YlGnBu",
        "Yellow-Green": "YlGn",
        "Yellow-Orange-Brown": "YlOrBr",
        "Yellow-Orange-Red": "YlOrRd",
        "Viridis": ["#440154","#440256","#450457","#450559","#46075a","#46085c","#460a5d","#460b5e","#470d60","#470e61","#471063","#471164","#471365","#481467","#481668","#481769","#48186a","#481a6c","#481b6d","#481c6e","#481d6f","#481f70","#482071","#482173","#482374","#482475","#482576","#482677","#482878","#482979","#472a7a","#472c7a","#472d7b","#472e7c","#472f7d","#46307e","#46327e","#46337f","#463480","#453581","#453781","#453882","#443983","#443a83","#443b84","#433d84","#433e85","#423f85","#424086","#424186","#414287","#414487","#404588","#404688","#3f4788","#3f4889","#3e4989","#3e4a89","#3e4c8a","#3d4d8a","#3d4e8a","#3c4f8a","#3c508b","#3b518b","#3b528b","#3a538b","#3a548c","#39558c","#39568c","#38588c","#38598c","#375a8c","#375b8d","#365c8d","#365d8d","#355e8d","#355f8d","#34608d","#34618d","#33628d","#33638d","#32648e","#32658e","#31668e","#31678e","#31688e","#30698e","#306a8e","#2f6b8e","#2f6c8e","#2e6d8e","#2e6e8e","#2e6f8e","#2d708e","#2d718e","#2c718e","#2c728e","#2c738e","#2b748e","#2b758e","#2a768e","#2a778e","#2a788e","#29798e","#297a8e","#297b8e","#287c8e","#287d8e","#277e8e","#277f8e","#27808e","#26818e","#26828e","#26828e","#25838e","#25848e","#25858e","#24868e","#24878e","#23888e","#23898e","#238a8d","#228b8d","#228c8d","#228d8d","#218e8d","#218f8d","#21908d","#21918c","#20928c","#20928c","#20938c","#1f948c","#1f958b","#1f968b","#1f978b","#1f988b","#1f998a","#1f9a8a","#1e9b8a","#1e9c89","#1e9d89","#1f9e89","#1f9f88","#1fa088","#1fa188","#1fa187","#1fa287","#20a386","#20a486","#21a585","#21a685","#22a785","#22a884","#23a983","#24aa83","#25ab82","#25ac82","#26ad81","#27ad81","#28ae80","#29af7f","#2ab07f","#2cb17e","#2db27d","#2eb37c","#2fb47c","#31b57b","#32b67a","#34b679","#35b779","#37b878","#38b977","#3aba76","#3bbb75","#3dbc74","#3fbc73","#40bd72","#42be71","#44bf70","#46c06f","#48c16e","#4ac16d","#4cc26c","#4ec36b","#50c46a","#52c569","#54c568","#56c667","#58c765","#5ac864","#5cc863","#5ec962","#60ca60","#63cb5f","#65cb5e","#67cc5c","#69cd5b","#6ccd5a","#6ece58","#70cf57","#73d056","#75d054","#77d153","#7ad151","#7cd250","#7fd34e","#81d34d","#84d44b","#86d549","#89d548","#8bd646","#8ed645","#90d743","#93d741","#95d840","#98d83e","#9bd93c","#9dd93b","#a0da39","#a2da37","#a5db36","#a8db34","#aadc32","#addc30","#b0dd2f","#b2dd2d","#b5de2b","#b8de29","#bade28","#bddf26","#c0df25","#c2df23","#c5e021","#c8e020","#cae11f","#cde11d","#d0e11c","#d2e21b","#d5e21a","#d8e219","#dae319","#dde318","#dfe318","#e2e418","#e5e419","#e7e419","#eae51a","#ece51b","#efe51c","#f1e51d","#f4e61e","#f6e620","#f8e621","#fbe723","#fde725"],
        "Inferno": ["#000004","#010005","#010106","#010108","#02010a","#02020c","#02020e","#030210","#040312","#040314","#050417","#060419","#07051b","#08051d","#09061f","#0a0722","#0b0724","#0c0826","#0d0829","#0e092b","#10092d","#110a30","#120a32","#140b34","#150b37","#160b39","#180c3c","#190c3e","#1b0c41","#1c0c43","#1e0c45","#1f0c48","#210c4a","#230c4c","#240c4f","#260c51","#280b53","#290b55","#2b0b57","#2d0b59","#2f0a5b","#310a5c","#320a5e","#340a5f","#360961","#380962","#390963","#3b0964","#3d0965","#3e0966","#400a67","#420a68","#440a68","#450a69","#470b6a","#490b6a","#4a0c6b","#4c0c6b","#4d0d6c","#4f0d6c","#510e6c","#520e6d","#540f6d","#550f6d","#57106e","#59106e","#5a116e","#5c126e","#5d126e","#5f136e","#61136e","#62146e","#64156e","#65156e","#67166e","#69166e","#6a176e","#6c186e","#6d186e","#6f196e","#71196e","#721a6e","#741a6e","#751b6e","#771c6d","#781c6d","#7a1d6d","#7c1d6d","#7d1e6d","#7f1e6c","#801f6c","#82206c","#84206b","#85216b","#87216b","#88226a","#8a226a","#8c2369","#8d2369","#8f2469","#902568","#922568","#932667","#952667","#972766","#982766","#9a2865","#9b2964","#9d2964","#9f2a63","#a02a63","#a22b62","#a32c61","#a52c60","#a62d60","#a82e5f","#a92e5e","#ab2f5e","#ad305d","#ae305c","#b0315b","#b1325a","#b3325a","#b43359","#b63458","#b73557","#b93556","#ba3655","#bc3754","#bd3853","#bf3952","#c03a51","#c13a50","#c33b4f","#c43c4e","#c63d4d","#c73e4c","#c83f4b","#ca404a","#cb4149","#cc4248","#ce4347","#cf4446","#d04545","#d24644","#d34743","#d44842","#d54a41","#d74b3f","#d84c3e","#d94d3d","#da4e3c","#db503b","#dd513a","#de5238","#df5337","#e05536","#e15635","#e25734","#e35933","#e45a31","#e55c30","#e65d2f","#e75e2e","#e8602d","#e9612b","#ea632a","#eb6429","#eb6628","#ec6726","#ed6925","#ee6a24","#ef6c23","#ef6e21","#f06f20","#f1711f","#f1731d","#f2741c","#f3761b","#f37819","#f47918","#f57b17","#f57d15","#f67e14","#f68013","#f78212","#f78410","#f8850f","#f8870e","#f8890c","#f98b0b","#f98c0a","#f98e09","#fa9008","#fa9207","#fa9407","#fb9606","#fb9706","#fb9906","#fb9b06","#fb9d07","#fc9f07","#fca108","#fca309","#fca50a","#fca60c","#fca80d","#fcaa0f","#fcac11","#fcae12","#fcb014","#fcb216","#fcb418","#fbb61a","#fbb81d","#fbba1f","#fbbc21","#fbbe23","#fac026","#fac228","#fac42a","#fac62d","#f9c72f","#f9c932","#f9cb35","#f8cd37","#f8cf3a","#f7d13d","#f7d340","#f6d543","#f6d746","#f5d949","#f5db4c","#f4dd4f","#f4df53","#f4e156","#f3e35a","#f3e55d","#f2e661","#f2e865","#f2ea69","#f1ec6d","#f1ed71","#f1ef75","#f1f179","#f2f27d","#f2f482","#f3f586","#f3f68a","#f4f88e","#f5f992","#f6fa96","#f8fb9a","#f9fc9d","#fafda1","#fcffa4"],
        "Magma": ["#000004","#010005","#010106","#010108","#020109","#02020b","#02020d","#03030f","#030312","#040414","#050416","#060518","#06051a","#07061c","#08071e","#090720","#0a0822","#0b0924","#0c0926","#0d0a29","#0e0b2b","#100b2d","#110c2f","#120d31","#130d34","#140e36","#150e38","#160f3b","#180f3d","#19103f","#1a1042","#1c1044","#1d1147","#1e1149","#20114b","#21114e","#221150","#241253","#251255","#271258","#29115a","#2a115c","#2c115f","#2d1161","#2f1163","#311165","#331067","#341069","#36106b","#38106c","#390f6e","#3b0f70","#3d0f71","#3f0f72","#400f74","#420f75","#440f76","#451077","#471078","#491078","#4a1079","#4c117a","#4e117b","#4f127b","#51127c","#52137c","#54137d","#56147d","#57157e","#59157e","#5a167e","#5c167f","#5d177f","#5f187f","#601880","#621980","#641a80","#651a80","#671b80","#681c81","#6a1c81","#6b1d81","#6d1d81","#6e1e81","#701f81","#721f81","#732081","#752181","#762181","#782281","#792282","#7b2382","#7c2382","#7e2482","#802582","#812581","#832681","#842681","#862781","#882781","#892881","#8b2981","#8c2981","#8e2a81","#902a81","#912b81","#932b80","#942c80","#962c80","#982d80","#992d80","#9b2e7f","#9c2e7f","#9e2f7f","#a02f7f","#a1307e","#a3307e","#a5317e","#a6317d","#a8327d","#aa337d","#ab337c","#ad347c","#ae347b","#b0357b","#b2357b","#b3367a","#b5367a","#b73779","#b83779","#ba3878","#bc3978","#bd3977","#bf3a77","#c03a76","#c23b75","#c43c75","#c53c74","#c73d73","#c83e73","#ca3e72","#cc3f71","#cd4071","#cf4070","#d0416f","#d2426f","#d3436e","#d5446d","#d6456c","#d8456c","#d9466b","#db476a","#dc4869","#de4968","#df4a68","#e04c67","#e24d66","#e34e65","#e44f64","#e55064","#e75263","#e85362","#e95462","#ea5661","#eb5760","#ec5860","#ed5a5f","#ee5b5e","#ef5d5e","#f05f5e","#f1605d","#f2625d","#f2645c","#f3655c","#f4675c","#f4695c","#f56b5c","#f66c5c","#f66e5c","#f7705c","#f7725c","#f8745c","#f8765c","#f9785d","#f9795d","#f97b5d","#fa7d5e","#fa7f5e","#fa815f","#fb835f","#fb8560","#fb8761","#fc8961","#fc8a62","#fc8c63","#fc8e64","#fc9065","#fd9266","#fd9467","#fd9668","#fd9869","#fd9a6a","#fd9b6b","#fe9d6c","#fe9f6d","#fea16e","#fea36f","#fea571","#fea772","#fea973","#feaa74","#feac76","#feae77","#feb078","#feb27a","#feb47b","#feb67c","#feb77e","#feb97f","#febb81","#febd82","#febf84","#fec185","#fec287","#fec488","#fec68a","#fec88c","#feca8d","#fecc8f","#fecd90","#fecf92","#fed194","#fed395","#fed597","#fed799","#fed89a","#fdda9c","#fddc9e","#fddea0","#fde0a1","#fde2a3","#fde3a5","#fde5a7","#fde7a9","#fde9aa","#fdebac","#fcecae","#fceeb0","#fcf0b2","#fcf2b4","#fcf4b6","#fcf6b8","#fcf7b9","#fcf9bb","#fcfbbd","#fcfdbf"],
        "Plasma": ["#0d0887","#100788","#130789","#16078a","#19068c","#1b068d","#1d068e","#20068f","#220690","#240691","#260591","#280592","#2a0593","#2c0594","#2e0595","#2f0596","#310597","#330597","#350498","#370499","#38049a","#3a049a","#3c049b","#3e049c","#3f049c","#41049d","#43039e","#44039e","#46039f","#48039f","#4903a0","#4b03a1","#4c02a1","#4e02a2","#5002a2","#5102a3","#5302a3","#5502a4","#5601a4","#5801a4","#5901a5","#5b01a5","#5c01a6","#5e01a6","#6001a6","#6100a7","#6300a7","#6400a7","#6600a7","#6700a8","#6900a8","#6a00a8","#6c00a8","#6e00a8","#6f00a8","#7100a8","#7201a8","#7401a8","#7501a8","#7701a8","#7801a8","#7a02a8","#7b02a8","#7d03a8","#7e03a8","#8004a8","#8104a7","#8305a7","#8405a7","#8606a6","#8707a6","#8808a6","#8a09a5","#8b0aa5","#8d0ba5","#8e0ca4","#8f0da4","#910ea3","#920fa3","#9410a2","#9511a1","#9613a1","#9814a0","#99159f","#9a169f","#9c179e","#9d189d","#9e199d","#a01a9c","#a11b9b","#a21d9a","#a31e9a","#a51f99","#a62098","#a72197","#a82296","#aa2395","#ab2494","#ac2694","#ad2793","#ae2892","#b02991","#b12a90","#b22b8f","#b32c8e","#b42e8d","#b52f8c","#b6308b","#b7318a","#b83289","#ba3388","#bb3488","#bc3587","#bd3786","#be3885","#bf3984","#c03a83","#c13b82","#c23c81","#c33d80","#c43e7f","#c5407e","#c6417d","#c7427c","#c8437b","#c9447a","#ca457a","#cb4679","#cc4778","#cc4977","#cd4a76","#ce4b75","#cf4c74","#d04d73","#d14e72","#d24f71","#d35171","#d45270","#d5536f","#d5546e","#d6556d","#d7566c","#d8576b","#d9586a","#da5a6a","#da5b69","#db5c68","#dc5d67","#dd5e66","#de5f65","#de6164","#df6263","#e06363","#e16462","#e26561","#e26660","#e3685f","#e4695e","#e56a5d","#e56b5d","#e66c5c","#e76e5b","#e76f5a","#e87059","#e97158","#e97257","#ea7457","#eb7556","#eb7655","#ec7754","#ed7953","#ed7a52","#ee7b51","#ef7c51","#ef7e50","#f07f4f","#f0804e","#f1814d","#f1834c","#f2844b","#f3854b","#f3874a","#f48849","#f48948","#f58b47","#f58c46","#f68d45","#f68f44","#f79044","#f79143","#f79342","#f89441","#f89540","#f9973f","#f9983e","#f99a3e","#fa9b3d","#fa9c3c","#fa9e3b","#fb9f3a","#fba139","#fba238","#fca338","#fca537","#fca636","#fca835","#fca934","#fdab33","#fdac33","#fdae32","#fdaf31","#fdb130","#fdb22f","#fdb42f","#fdb52e","#feb72d","#feb82c","#feba2c","#febb2b","#febd2a","#febe2a","#fec029","#fdc229","#fdc328","#fdc527","#fdc627","#fdc827","#fdca26","#fdcb26","#fccd25","#fcce25","#fcd025","#fcd225","#fbd324","#fbd524","#fbd724","#fad824","#fada24","#f9dc24","#f9dd25","#f8df25","#f8e125","#f7e225","#f7e425","#f6e626","#f6e826","#f5e926","#f5eb27","#f4ed27","#f3ee27","#f3f027","#f2f227","#f1f426","#f1f525","#f0f724","#f0f921"],
        "Warm": ["#6e40aa","#6f40aa","#7140ab","#723fac","#743fac","#753fad","#773fad","#783fae","#7a3fae","#7c3faf","#7d3faf","#7f3faf","#803eb0","#823eb0","#833eb0","#853eb1","#873eb1","#883eb1","#8a3eb2","#8b3eb2","#8d3eb2","#8f3db2","#903db2","#923db3","#943db3","#953db3","#973db3","#983db3","#9a3db3","#9c3db3","#9d3db3","#9f3db3","#a13db3","#a23db3","#a43db3","#a63cb3","#a73cb3","#a93cb3","#aa3cb2","#ac3cb2","#ae3cb2","#af3cb2","#b13cb2","#b23cb1","#b43cb1","#b63cb1","#b73cb0","#b93cb0","#ba3cb0","#bc3caf","#be3caf","#bf3caf","#c13dae","#c23dae","#c43dad","#c53dad","#c73dac","#c83dac","#ca3dab","#cb3daa","#cd3daa","#ce3da9","#d03ea9","#d13ea8","#d33ea7","#d43ea7","#d53ea6","#d73ea5","#d83fa4","#da3fa4","#db3fa3","#dc3fa2","#de3fa1","#df40a0","#e040a0","#e2409f","#e3409e","#e4419d","#e5419c","#e7419b","#e8429a","#e94299","#ea4298","#eb4397","#ed4396","#ee4395","#ef4494","#f04493","#f14592","#f24591","#f34590","#f4468f","#f5468e","#f6478d","#f7478c","#f8488b","#f9488a","#fa4988","#fb4987","#fc4a86","#fd4a85","#fe4b84","#fe4b83","#ff4c81","#ff4d80","#ff4d7f","#ff4e7e","#ff4e7d","#ff4f7b","#ff507a","#ff5079","#ff5178","#ff5276","#ff5275","#ff5374","#ff5473","#ff5572","#ff5570","#ff566f","#ff576e","#ff586d","#ff586b","#ff596a","#ff5a69","#ff5b68","#ff5c66","#ff5d65","#ff5d64","#ff5e63","#ff5f61","#ff6060","#ff615f","#ff625e","#ff635d","#ff645b","#ff655a","#ff6659","#ff6758","#ff6857","#ff6956","#ff6a54","#ff6b53","#ff6c52","#ff6d51","#ff6e50","#ff6f4f","#ff704e","#ff714d","#ff724c","#ff734b","#ff744a","#ff7549","#ff7648","#ff7847","#ff7946","#ff7a45","#ff7b44","#ff7c43","#ff7d42","#ff7e41","#ff8040","#ff813f","#ff823e","#ff833d","#ff843d","#ff863c","#ff873b","#ff883a","#ff893a","#ff8a39","#ff8c38","#ff8d37","#ff8e37","#ff8f36","#fe9136","#fd9235","#fd9334","#fc9534","#fb9633","#fa9733","#f99832","#f99a32","#f89b32","#f79c31","#f69d31","#f59f30","#f4a030","#f3a130","#f2a32f","#f1a42f","#f0a52f","#efa62f","#eea82f","#eda92e","#ecaa2e","#ebac2e","#eaad2e","#e9ae2e","#e8b02e","#e7b12e","#e6b22e","#e5b32e","#e4b52e","#e3b62e","#e2b72f","#e1b92f","#e0ba2f","#dfbb2f","#debc30","#ddbe30","#dbbf30","#dac030","#d9c131","#d8c331","#d7c432","#d6c532","#d5c633","#d4c833","#d3c934","#d2ca34","#d1cb35","#cfcc36","#cece36","#cdcf37","#ccd038","#cbd138","#cad239","#c9d33a","#c8d53b","#c7d63c","#c6d73c","#c5d83d","#c4d93e","#c3da3f","#c2db40","#c1dc41","#c0dd42","#bfdf43","#bee044","#bde146","#bce247","#bbe348","#bae449","#b9e54a","#b8e64b","#b7e74d","#b6e84e","#b6e94f","#b5ea51","#b4ea52","#b3eb53","#b2ec55","#b1ed56","#b1ee58","#b0ef59","#aff05b"],
        "Cool": ["#6e40aa","#6d41ab","#6d41ad","#6d42ae","#6c43af","#6c43b0","#6b44b2","#6b45b3","#6a46b4","#6a46b5","#6a47b7","#6948b8","#6849b9","#684aba","#674abb","#674bbd","#664cbe","#664dbf","#654ec0","#654fc1","#6450c2","#6350c3","#6351c4","#6252c5","#6153c6","#6154c7","#6055c8","#5f56c9","#5f57ca","#5e58cb","#5d59cc","#5c5acd","#5c5bce","#5b5ccf","#5a5dd0","#595ed1","#595fd1","#5860d2","#5761d3","#5662d4","#5663d5","#5564d5","#5465d6","#5366d7","#5267d7","#5168d8","#5169d9","#506ad9","#4f6bda","#4e6cda","#4d6ddb","#4c6edb","#4b70dc","#4b71dc","#4a72dd","#4973dd","#4874de","#4775de","#4676df","#4577df","#4479df","#447adf","#437be0","#427ce0","#417de0","#407ee0","#3f80e1","#3e81e1","#3d82e1","#3d83e1","#3c84e1","#3b86e1","#3a87e1","#3988e1","#3889e1","#378ae1","#378ce1","#368de1","#358ee1","#348fe1","#3390e1","#3292e1","#3293e1","#3194e0","#3095e0","#2f96e0","#2e98e0","#2e99df","#2d9adf","#2c9bdf","#2b9cde","#2b9ede","#2a9fdd","#29a0dd","#29a1dd","#28a2dc","#27a4dc","#26a5db","#26a6db","#25a7da","#25a8d9","#24aad9","#23abd8","#23acd8","#22add7","#22aed6","#21afd5","#21b1d5","#20b2d4","#20b3d3","#1fb4d2","#1fb5d2","#1eb6d1","#1eb8d0","#1db9cf","#1dbace","#1dbbcd","#1cbccc","#1cbdcc","#1cbecb","#1bbfca","#1bc0c9","#1bc2c8","#1ac3c7","#1ac4c6","#1ac5c5","#1ac6c4","#1ac7c2","#1ac8c1","#19c9c0","#19cabf","#19cbbe","#19ccbd","#19cdbc","#19cebb","#19cfb9","#19d0b8","#19d1b7","#19d2b6","#19d3b5","#1ad4b4","#1ad5b2","#1ad5b1","#1ad6b0","#1ad7af","#1bd8ad","#1bd9ac","#1bdaab","#1bdbaa","#1cdba8","#1cdca7","#1cdda6","#1ddea4","#1ddfa3","#1edfa2","#1ee0a0","#1fe19f","#1fe29e","#20e29d","#20e39b","#21e49a","#22e599","#22e597","#23e696","#24e795","#24e793","#25e892","#26e891","#27e98f","#27ea8e","#28ea8d","#29eb8c","#2aeb8a","#2bec89","#2cec88","#2ded87","#2eed85","#2fee84","#30ee83","#31ef82","#32ef80","#33f07f","#34f07e","#35f07d","#37f17c","#38f17a","#39f279","#3af278","#3bf277","#3df376","#3ef375","#3ff374","#41f373","#42f471","#43f470","#45f46f","#46f46e","#48f56d","#49f56c","#4bf56b","#4cf56a","#4ef56a","#4ff669","#51f668","#52f667","#54f666","#55f665","#57f664","#59f664","#5af663","#5cf662","#5ef661","#5ff761","#61f760","#63f75f","#64f75f","#66f75e","#68f75d","#6af75d","#6bf65c","#6df65c","#6ff65b","#71f65b","#73f65a","#74f65a","#76f659","#78f659","#7af659","#7cf658","#7ef658","#80f558","#81f558","#83f557","#85f557","#87f557","#89f557","#8bf457","#8df457","#8ff457","#91f457","#93f457","#94f357","#96f357","#98f357","#9af357","#9cf257","#9ef258","#a0f258","#a2f258","#a4f158","#a6f159","#a8f159","#aaf159","#abf05a","#adf05a","#aff05b"],
        "CubeHelixDefault": ["#000000","#020102","#030103","#050205","#070206","#080308","#0a030a","#0b040c","#0c050e","#0e050f","#0f0611","#100713","#110815","#120817","#130919","#140a1b","#150b1d","#160c1f","#160d21","#170e23","#180f25","#181027","#191129","#19122b","#19132d","#1a142f","#1a1631","#1a1733","#1a1835","#1b1a36","#1b1b38","#1b1c3a","#1b1e3b","#1b1f3d","#1a213e","#1a2240","#1a2441","#1a2543","#1a2744","#192845","#192a46","#192c47","#192d48","#182f49","#18314a","#18324b","#17344c","#17364c","#17374d","#16394d","#163b4e","#163d4e","#163f4e","#16404e","#15424e","#15444f","#15464e","#15474e","#15494e","#154b4e","#154d4e","#154e4d","#15504d","#15524c","#16534c","#16554b","#16574b","#17584a","#175a49","#185b48","#195d48","#195e47","#1a6046","#1b6145","#1c6344","#1d6443","#1e6542","#1f6741","#206840","#22693f","#236a3e","#256b3d","#266c3c","#286d3b","#2a6e3a","#2b6f39","#2d7038","#2f7137","#317236","#337335","#357435","#387434","#3a7533","#3c7632","#3f7632","#417731","#447731","#467830","#497830","#4c792f","#4e792f","#51792f","#54792f","#577a2f","#5a7a2f","#5d7a2f","#607a2f","#637a2f","#667a30","#697b30","#6c7b31","#6f7b31","#727b32","#757b33","#787b34","#7b7a35","#7e7a36","#817a37","#847a38","#877a3a","#8a7a3b","#8d7a3d","#907a3e","#937a40","#967a42","#997944","#9c7946","#9f7948","#a1794a","#a4794c","#a7794f","#a97951","#ac7954","#ae7956","#b17959","#b3795b","#b5795e","#b77961","#b97964","#bc7967","#be796a","#bf796d","#c17a70","#c37a73","#c57a76","#c67a79","#c87b7c","#c97b7f","#ca7c83","#cc7c86","#cd7d89","#ce7d8c","#cf7e8f","#d07e93","#d17f96","#d18099","#d2809c","#d381a0","#d382a3","#d383a6","#d484a9","#d485ac","#d486af","#d487b2","#d588b5","#d589b8","#d48abb","#d48cbe","#d48dc1","#d48ec3","#d490c6","#d391c9","#d392cb","#d294ce","#d295d0","#d297d2","#d198d4","#d09ad7","#d09cd9","#cf9ddb","#cf9fdd","#cea1df","#cda2e0","#cca4e2","#cca6e4","#cba8e5","#caa9e7","#caabe8","#c9ade9","#c8afea","#c8b1ec","#c7b2ed","#c6b4ee","#c6b6ee","#c5b8ef","#c5baf0","#c4bcf1","#c4bdf1","#c3bff2","#c3c1f2","#c2c3f2","#c2c5f3","#c2c6f3","#c2c8f3","#c1caf3","#c1ccf3","#c1cdf3","#c1cff3","#c1d1f3","#c2d2f3","#c2d4f3","#c2d6f3","#c2d7f3","#c3d9f3","#c3daf2","#c4dcf2","#c4ddf2","#c5dff2","#c6e0f1","#c6e1f1","#c7e3f1","#c8e4f0","#c9e5f0","#cae7f0","#cbe8f0","#cce9ef","#cdeaef","#cfebef","#d0ecef","#d1edef","#d3eeef","#d4efef","#d6f0ef","#d7f1ef","#d9f2ef","#dbf3ef","#dcf3ef","#def4ef","#e0f5f0","#e2f6f0","#e3f6f0","#e5f7f1","#e7f8f1","#e9f8f2","#ebf9f3","#edfaf4","#effaf4","#f0fbf5","#f2fbf6","#f4fcf7","#f6fcf8","#f8fdfa","#fafdfb","#fbfefc","#fdfefe","#ffffff"],
        "Brown-Blue-Green": "BrBG",
        "Purple-Red-Green": "PRGn",
        "Pink-Yellow-Green": "PiYG",
        "Purple-Orange": "PuOr",
        "Red-Blue": "RdBu",
        "Red-Grey": "RdGy",
        "Red-Yellow-Blue": "RdYlBu",
        "Red-Yellow-Green": "RdYlGn",
        "Spectral": "Spectral",
        "Rainbow": ["#6e40aa","#7140ab","#743fac","#773fad","#7a3fae","#7d3faf","#803eb0","#833eb0","#873eb1","#8a3eb2","#8d3eb2","#903db2","#943db3","#973db3","#9a3db3","#9d3db3","#a13db3","#a43db3","#a73cb3","#aa3cb2","#ae3cb2","#b13cb2","#b43cb1","#b73cb0","#ba3cb0","#be3caf","#c13dae","#c43dad","#c73dac","#ca3dab","#cd3daa","#d03ea9","#d33ea7","#d53ea6","#d83fa4","#db3fa3","#de3fa1","#e040a0","#e3409e","#e5419c","#e8429a","#ea4298","#ed4396","#ef4494","#f14592","#f34590","#f5468e","#f7478c","#f9488a","#fb4987","#fd4a85","#fe4b83","#ff4d80","#ff4e7e","#ff4f7b","#ff5079","#ff5276","#ff5374","#ff5572","#ff566f","#ff586d","#ff596a","#ff5b68","#ff5d65","#ff5e63","#ff6060","#ff625e","#ff645b","#ff6659","#ff6857","#ff6a54","#ff6c52","#ff6e50","#ff704e","#ff724c","#ff744a","#ff7648","#ff7946","#ff7b44","#ff7d42","#ff8040","#ff823e","#ff843d","#ff873b","#ff893a","#ff8c38","#ff8e37","#fe9136","#fd9334","#fb9633","#f99832","#f89b32","#f69d31","#f4a030","#f2a32f","#f0a52f","#eea82f","#ecaa2e","#eaad2e","#e8b02e","#e6b22e","#e4b52e","#e2b72f","#e0ba2f","#debc30","#dbbf30","#d9c131","#d7c432","#d5c633","#d3c934","#d1cb35","#cece36","#ccd038","#cad239","#c8d53b","#c6d73c","#c4d93e","#c2db40","#c0dd42","#bee044","#bce247","#bae449","#b8e64b","#b6e84e","#b5ea51","#b3eb53","#b1ed56","#b0ef59","#adf05a","#aaf159","#a6f159","#a2f258","#9ef258","#9af357","#96f357","#93f457","#8ff457","#8bf457","#87f557","#83f557","#80f558","#7cf658","#78f659","#74f65a","#71f65b","#6df65c","#6af75d","#66f75e","#63f75f","#5ff761","#5cf662","#59f664","#55f665","#52f667","#4ff669","#4cf56a","#49f56c","#46f46e","#43f470","#41f373","#3ef375","#3bf277","#39f279","#37f17c","#34f07e","#32ef80","#30ee83","#2eed85","#2cec88","#2aeb8a","#28ea8d","#27e98f","#25e892","#24e795","#22e597","#21e49a","#20e29d","#1fe19f","#1edfa2","#1ddea4","#1cdca7","#1bdbaa","#1bd9ac","#1ad7af","#1ad5b1","#1ad4b4","#19d2b6","#19d0b8","#19cebb","#19ccbd","#19cabf","#1ac8c1","#1ac6c4","#1ac4c6","#1bc2c8","#1bbfca","#1cbdcc","#1dbbcd","#1db9cf","#1eb6d1","#1fb4d2","#20b2d4","#21afd5","#22add7","#23abd8","#25a8d9","#26a6db","#27a4dc","#29a1dd","#2a9fdd","#2b9cde","#2d9adf","#2e98e0","#3095e0","#3293e1","#3390e1","#358ee1","#378ce1","#3889e1","#3a87e1","#3c84e1","#3d82e1","#3f80e1","#417de0","#437be0","#4479df","#4676df","#4874de","#4a72dd","#4b70dc","#4d6ddb","#4f6bda","#5169d9","#5267d7","#5465d6","#5663d5","#5761d3","#595fd1","#5a5dd0","#5c5bce","#5d59cc","#5f57ca","#6055c8","#6153c6","#6351c4","#6450c2","#654ec0","#664cbe","#674abb","#6849b9","#6a47b7","#6a46b4","#6b44b2","#6c43af","#6d41ad","#6e40aa"],
        "Sinebow": ["#ff4040","#ff423d","#ff453a","#ff4838","#fe4b35","#fe4e33","#fe5130","#fd542e","#fd572b","#fc5a29","#fb5d27","#fa6025","#f96322","#f96620","#f7691e","#f66c1c","#f56f1a","#f47218","#f37517","#f17815","#f07c13","#ee7f11","#ed8210","#eb850e","#e9880d","#e88b0c","#e68e0a","#e49209","#e29508","#e09807","#de9b06","#dc9e05","#d9a104","#d7a403","#d5a703","#d2aa02","#d0ad02","#ceb001","#cbb301","#c9b600","#c6b800","#c3bb00","#c1be00","#bec100","#bbc300","#b8c600","#b6c900","#b3cb01","#b0ce01","#add002","#aad202","#a7d503","#a4d703","#a1d904","#9edc05","#9bde06","#98e007","#95e208","#92e409","#8ee60a","#8be80c","#88e90d","#85eb0e","#82ed10","#7fee11","#7cf013","#78f115","#75f317","#72f418","#6ff51a","#6cf61c","#69f71e","#66f920","#63f922","#60fa25","#5dfb27","#5afc29","#57fd2b","#54fd2e","#51fe30","#4efe33","#4bfe35","#48ff38","#45ff3a","#42ff3d","#40ff40","#3dff42","#3aff45","#38ff48","#35fe4b","#33fe4e","#30fe51","#2efd54","#2bfd57","#29fc5a","#27fb5d","#25fa60","#22f963","#20f966","#1ef769","#1cf66c","#1af56f","#18f472","#17f375","#15f178","#13f07c","#11ee7f","#10ed82","#0eeb85","#0de988","#0ce88b","#0ae68e","#09e492","#08e295","#07e098","#06de9b","#05dc9e","#04d9a1","#03d7a4","#03d5a7","#02d2aa","#02d0ad","#01ceb0","#01cbb3","#00c9b6","#00c6b8","#00c3bb","#00c1be","#00bec1","#00bbc3","#00b8c6","#00b6c9","#01b3cb","#01b0ce","#02add0","#02aad2","#03a7d5","#03a4d7","#04a1d9","#059edc","#069bde","#0798e0","#0895e2","#0992e4","#0a8ee6","#0c8be8","#0d88e9","#0e85eb","#1082ed","#117fee","#137cf0","#1578f1","#1775f3","#1872f4","#1a6ff5","#1c6cf6","#1e69f7","#2066f9","#2263f9","#2560fa","#275dfb","#295afc","#2b57fd","#2e54fd","#3051fe","#334efe","#354bfe","#3848ff","#3a45ff","#3d42ff","#4040ff","#423dff","#453aff","#4838ff","#4b35fe","#4e33fe","#5130fe","#542efd","#572bfd","#5a29fc","#5d27fb","#6025fa","#6322f9","#6620f9","#691ef7","#6c1cf6","#6f1af5","#7218f4","#7517f3","#7815f1","#7c13f0","#7f11ee","#8210ed","#850eeb","#880de9","#8b0ce8","#8e0ae6","#9209e4","#9508e2","#9807e0","#9b06de","#9e05dc","#a104d9","#a403d7","#a703d5","#aa02d2","#ad02d0","#b001ce","#b301cb","#b600c9","#b800c6","#bb00c3","#be00c1","#c100be","#c300bb","#c600b8","#c900b6","#cb01b3","#ce01b0","#d002ad","#d202aa","#d503a7","#d703a4","#d904a1","#dc059e","#de069b","#e00798","#e20895","#e40992","#e60a8e","#e80c8b","#e90d88","#eb0e85","#ed1082","#ee117f","#f0137c","#f11578","#f31775","#f41872","#f51a6f","#f61c6c","#f71e69","#f92066","#f92263","#fa2560","#fb275d","#fc295a","#fd2b57","#fd2e54","#fe3051","#fe334e","#fe354b","#ff3848","#ff3a45","#ff3d42","#ff4040"],
    };

    for (const [key, value] of Object.entries(colorBrewerList)) {
        // console.log("Creating: " + key, value);
        var pattern = Trianglify({
            cell_size: 1000,
            variance: "1",
            x_colors: value,
            width: 15000,
            height: 15000
        });
        // pattern = pattern.png()
        patternDict[key] = pattern;
    }
    return patternDict;
}

async function saveGeneratedPatterns(patternDict) {
    for (const [key, value] of Object.entries(patternDict)) {
        console.log("Waiting to download", key, value);
        // await sleep(5000);
        console.log("Starting download", key, value);
        var pngToSave = value.png();
        // pngToSave.remove();
        // saveBase64AsFile(value.png(), key + ".png");
    }
}

function generateAndSavePatterns() {
    var patternDict = {};
    patternDict = generateDictOfPatterns(patternDict);
    // console.log(patternDict);

    saveGeneratedPatterns(patternDict);

}

