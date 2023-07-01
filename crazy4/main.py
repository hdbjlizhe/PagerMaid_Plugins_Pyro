from secrets import choice

from pagermaid.listener import listener
from pagermaid.enums import Message

crazy4_data = [
    "大家好，我是秦始皇，其实我并没有死，我在西安有100000吨黄金，今天肯德基疯狂星期四，我现在需要有人来请我吃29.9块钱8只蛋挞。我明天直接带部队复活，让你统领三军！",
    "花2000w可以让lex账号解封\n花200w可以让hololive回归\n花20w可以给东雪莲上10个月总督\n花2w可以让女生不用在厕所生孩子\n花2000可以去华东理工大学买一副耳机\n花200可以买一副VR眼睛在厕所求导\n那花50呢？能让我愉快的渡过一个疯狂星期四吗？\n可以，KFC疯狂星期四鸡排桶仅需49.9！\nV我50，助我度过一个快乐的疯狂星期四！",
    "我是盗号的 我把这个人的号盗了 但是我看了这个人的聊天记录 发现他过得非常艰苦 他的吃住一直很烂 我看到大家的生活都很富足 我希望有人看见了能救济他一下 请他吃一顿肯德基疯狂星期四 就这样吧 眼眶都湿润了 我下了",
    "离婚这么多年了，竟然在群里遇到你了，你过得挺好我也就放心了。孩子上四年级了，成绩一直都很好，连续三年拿班上第一名，就是性格像你，每次生气就逃避，孩子总问妈妈什么时候来参加家长会！有时间就来看看孩子吧，多陪陪孩子，孩子今天想吃肯德基，因为今天是肯德基疯狂星期四，v我40，我请孩子吃。",
    "扒个群里的渣男，我有个朋友被群友睡了，大概在三个月以前吧，我朋友在群里认识了一个男的，他们在网上聊了差不多两个星期左右就见面了，而且第一次见面就去了宾馆，之后的每个星期六日都会去，就这样持续了好几个月。我朋友给那个男的说，已经一个多月没来大姨妈了，想不到这句话说完，隔天就找不到男的了，手机一直打不通，关机，直到我朋友前几天跟父母坦白这件事情，那天晚上我偷偷给她买了验孕棒一看，真怀孕了。然后我第二天请假一天，专门跟她聊这个事，她说那个男的对她很好很好什么的，我说对你好还不是想玩你，实在不行就报警吧。她当时听完这句话就趴桌子上大哭。正当我打开手机想报警的时候，不小心打开了肯德基，想起来今天原来是疯狂星期四，所以说谁请我肯德基？吃完我继续说",
    "实不相瞒我结婚七年了，他不爱我也不放过我，孩子从小被H集团幕后掌托人也就是他爷爷奶奶带走，所有人都阻拦我见孩子，一场车祸我失去了所有记忆，只记得我好想他，夜不能寐，茶饭不思，寝食难安，重复做着我带着他去吃肯德基疯狂星期四的梦，所以能请我吃肯德基疯狂星期四帮我恢复丢失的记忆吗……",
    "袜！好神奇的功能耶！私信给我发送“疯狂星期四”就可以得到我的一句“你请我吃”！真的好神奇！！友友们快来试试吧！！！",
    "狗的叫声是汪汪汪 猫的叫声是喵喵喵 牛的叫声是all I want for Christmas is you 星期四的叫声是抽一位幸运儿请我肯德基疯狂星期四",
    "我都明白 我是选项E 我是planB 是分叉的头发 洗衣机流出的泡沫 超市里被捏碎的饼干 是吃腻的奶油 是落寞的城市 是地上的草 我是被踩踏的 是西装的备用扣 是被雨淋湿的小狗  是腐烂的橘子 是过期的牛奶 是断线的风筝 是被随意丢弃的向日葵 是沉默寡言的小朋友 所以能v我40吗 今天肯德基疯狂星期四",
    "穿过挪威的森林，让我走进你的梦里，夕阳落在我的铠甲，王子不一定骑白马，现在是中午十二点四十四分，你不必故作冷淡，我也不想做最后的纠缠。最后问一句，疯狂星期四，谁请我吃肯德基？",
    "刚给女朋友洗完衣服 手搓的 平时洗之前手要消5遍毒 今天因为漏了一遍被女朋友打了两巴掌 现在心里有点委屈 今天我决定反击疯狂星期四 吮指原味鸡9.9两块 葡式蛋挞 8块29.9 黄金鸡块20块19.9谁请我吃 我边吃边跟你说我平时在家里都怎么受罪的",
    "肯德基给你们多少钱了，让你们周周给编段子，疯狂星期四真的那么有诱惑力？我偏不信，v我50，我去试试",
    "我本是显赫世家的奥特曼，却被诡计多端的怪兽所害！奥特曼家族弃我！奥特之父逐我！甚至断我伽马射线！重生一世，今天肯德基疯狂星期四！谁请我吃？",
    "蛮讽刺的，从凌晨开始等到现在，没有一个人和我说生日快乐，我的亲人没有说，朋友也没有说，我最在乎的人也没有说，直到现在我才明白原来今天不是我生日。但是今天是肯德基疯狂星期四！谁请我吃？",
    "我独自一人远离家乡来到成都上学，同学欺我，老师骂我，舍友打我，我流浪在晨风街头，衣衫褴褛，身无分文，活得不如一条流浪狗。天地浩大，却没有我的容身之处。我想问一问苍天，今天肯德基疯狂星期四，谁请我吃？",
    "老师问三个学生，你们用什么东西可以填满一整个房间。第一个学生找来稻草铺满地板，老师摇了摇头。第二个学生找来一根蜡烛点燃，屋子里充满了光，老师还是摇了摇头，因为学生的影子没有被照到。这时第三个学生拿出肯德基疯狂星期四的黄金小酥肉，顿时香味充满了整个房间",
    "肯德基这逼养的，怎么又到了星期四，我开始留头发，减重，换风格，开始往前冲，不好意思啊，这一次，肯德基疯狂星期四，我一定要吃。我本是显赫世家的少爷，却被诡计多端的奸人所害！家人弃我！师门逐我！甚至断我灵脉！重生一世，今天肯德基疯狂星期四！谁请我吃？Bro别他妈垂头丧气了知道今天是什么日子吗？今天是肯德基fucking crazy Thursday！吮指原味鸡30块钱4个Bro，v我60，我他妈要吃8个。",
    "我想问一下大家，之前朋友找我借钱，前后加起来有大概七万（够立案）但是没有借条也没有字据，微信也早已互删没有任何关于借的字眼，只有支付宝上还有转账记录，我妈刚让我把转账记录发给他看一下的时候，我点支付宝点歪了，不小心点开了肯德基，发现今天是疯狂星期四，谁请我吃？",
    "我在兰州拉面馆愤怒的甩开了筷子\n-老板，怎么一点肉没有  \n-穷逼事儿还挺多，十几块你能吃到什么肉？\n被羞辱的我，痛苦，落泪，难受，突然 我看到了一个广告：19.9，疯狂星期四，20个鸡块，兰州拉面一周的肉量！谁！谁请我吃！",
    "被群成员冷暴力半年，最近没有怎么哭了，慢慢变好了……以前有多快乐，现在就有多难过。从人间烟火的日常，到红着眼睛告别，消失在彼此的世界里，很痛，也很难。今天是肯德基疯狂星期四，v我60，抚慰我支离破碎的心",
    "最讨厌网络乞丐了，想吃星期四疯狂肯德基的不会自己买吗，什么都伸手要，觉得我说的对的请给我点一份。",
    "你跟你女朋友开房，裤子一脱你女朋友花容失色的质问你：你不是说你有18cm吗？怎么这么小？你说：因为今天是肯德基疯狂星期四活动满18减15。",
    "前段时间为了提升自己的文化素养，我给自己报了个书法培训班。因为跟我同期的都是小学生所以大家就有点排挤我，看不上我这么大年纪还在学这个。本来也没什么，但小学生的恶意真的超乎我的想象，他们说我老女人半只脚进棺材还来学书法，我听到都气哭了。我擦干眼眼泪不管他们继续练字，我发誓我一定要练出一笔好字，不能让钱白花。我凝神静气，在纸上认真写出了一行字：今天肯德基疯狂星期四，谁请我吃？",
    "我有时候会觉得大家并不喜欢那个真正的我。在网络上，我总是善于伪装，看起来每天都很快乐，无忧无虑，没有烦恼。我的生活也看起来很简单，没有很多人向往的灯红酒绿，纸醉金迷。我很宅，喜欢打游戏，现实中的我并不像网上这么有趣。我其实话很少，最爱干的事是一个人发呆。这样枯燥的我，真的会被大家喜欢吗？我很疑惑。\n如果你们能一层一层剥开我的内心，你们会发现，那颗心里写满了一句话：今天肯德基疯狂星期四，谁请我吃？",
    "生了孩子以后一直瘦不下去，老公像变了一个人似的，对我又打又骂，我好恨他，正当我打开手机想报警的时候，不小心打开了肯德基，想起来今天原来是疯狂星期四，所以说谁请我肯德基？吃完我继续讲",
    "他本是豪门少爷\n在新婚前夜却发现未婚妻和兄弟在喜床上翻滚\n她深夜买醉却撞上醉酒的他\n一夜痴缠他醒来后不见她的踪影\n只见床头压着一张纸：\n今 天 肯 德 基 疯 狂 星 期 四",
    "家人们，求助\n12月求姻缘应该去哪个寺庙？\nA、灵隐寺\nB、弘法寺\nC、甘露寺\nD、肯德基疯狂星期寺 ",
    "某个人不回消息永远别回了，终究是我不重要了吗？难道你心里就不明白吗？不然我整天闲得来找你聊天，我不会找别人聊天吗？你以为我天天闲得慌吗？我如此的喜欢你，你却对我无动于衷，这甜甜的恋爱，你到底打不打算要了？如果你还在意我，今天肯德基疯狂星期四，如果请我吃，我就原谅你",
    "时间让我长了年岁，却没有让我成为一个合格的大人。我以为我的十八岁，会工作稳定，收入可观，和喜欢的人去看山河大海，落日余晖。没想到，到了谈婚论嫁的年龄，我却仍在找自己的路上。今天肯德基疯狂星期四，谁请我吃？",
    "消息回得慢大家请理解，今天疯狂星期四，我在炸吮指原味鸡！",
    "我本是上市公司的老总，却被诡计多端的奸人所害！下属弃我！股东逐我！甚至清空我的股份！重来一生，我只想夺回我的公司！今天肯德基疯狂星期四，谁请我吃？",
    "后来不是报警了吗！那个男的隔了一个星期才找到，把他的父母和我朋友的父母喊到警察局里商量这件事到底怎么办，要不就结婚把这个孩子生下来，要么就打掉并赔偿我朋友30w，男方不想要这个孩子，但是父母手头也没有这多钱，硬着头皮跟我朋友结婚了，彩礼才拿了八万，结婚后男的经常不归家，在外面玩，我朋友挺着大肚子在家真的不容易，然后我实在看不下去了，就去照顾我朋友，我准备拿起手机给他打电话，又不小心点开肯德基，才想起来今天是肯德基Fucking Crazy Thursday疯狂星期四，谁请我吃我继续说",
    "男朋友跟我分手了，我心碎了决定见她一面把事情说清楚如果她非要分手我也无话可说。到了她家门口，死活不出来。我只是一片凋零的落叶，随着风飘落，我时常在想我的凋零是我自己的选择，还是风不挽留，就像茫茫大海里的一条孤单的鱼没有人会关心我，没有人会想念我。如果有一天我被人类发现，也许是我的生命走到了尽头，人类是贪婪的，是有欲望的，鱼在他们眼里是无尽的财富海洋资源在他们眼里是赖以生存的摇钱树，有人捕鱼，有人抓蚌壳，蚌壳那么不容易，她用自己的血肉磨出了珍珠，一颗又一颗，说到珍珠，你愿不愿意转我十块钱买一杯珍珠奶茶给我这条小鱼，哎看来我是一条无人疼爱的小鱼，不过是一条无人关心无人疼爱无人喜欢无人给我买奶茶的可怜巴巴的小鱼。我心如死灰在大街上游荡，打开手机看到了我们的恩爱时光泪流满面，忽然注意到手机上显示的时间，才发现今天是肯德基疯狂星期四，谁请我吃？",
    "我本是夜上海的一名贫穷又自强的黄包车夫，看遍了这个城市的繁华和热闹，也体验了这个社会的冷漠与无情。直到那一天，我的车上坐上了一位穿着四季歌的千金小姐，我感到了我平静已久的内心再一次颤动，我知道不应该，但我却还是爱上了。我知道我的身份地位配不上她，只求有个好心人给我39.9，让我买一个疯狂星期四热辣鸡桶，带给她舔狗的关怀。",
    "今天，是我人生中最黑暗，最emo的时候，但是我很难把朋友当成垃圾桶或者树洞去倾诉，更喜欢憋着自己消化，睡一觉第二天醒来就好了，不想连累别人不想把负面情绪传递给身边的朋友。但是，我更希望朋友能够给予我物质层面的帮助，今天是肯德基疯狂星期四，有哪个朋友愿意请我吃肯德基吗？",
    "你不用故作冷淡，我没有想过继续纠缠你了，最后一次了，真的，最后一次了，借我10元子,今天是肯德基疯狂星期四吮指原味鸡+黄金脆皮鸡才九块九，我是真的不想错过。",
    "扒个群里的渣女，我有个朋友被群友睡了，大概是三个月以前吧，我朋友在群里认识了一个女的，他们在网上聊了差不多两个星期左右就见面了，而且第一次见面就去宾馆了 ，之后的每个星期六星期天都会去，就这样持续了好几个月，我朋友给那个女的说，已经一个多月没奖励自己了，想不到这句话说完，隔天就找不到那个女的了，手机一直打不通，关机，直到我朋友前几天跟她父母坦白这件事情，我朋友就在旁边一直哭，那天晚上我偷偷给他买了个石原里美同款，还是没奖励自己了，然后我第二天请假一天,专门给他聊这个事，他说那个女的对他很好很好什么的，我说对你好还不是想玩你，实在不行抱树吧，他当时听完这句话就趴桌子上大哭，正当我打开手机想抱树的时候，不小心打开了肯德基，想起来今天原来是肯德基疯狂星期四，所以说谁请我肯德基？吃完我继续说",
    "吃完后，她下决心去打掉这个负心汉的孩子，到医院检查后发现并没有怀孕，此刻的她不知是喜是悲；出了医院门口，她心里五味杂陈，决定再打最后一次电话就放过自己，电话竟然接通了，接电话的是个陌生男声，说机主癌症晚期已经去世，整理遗物时发现了没电的手机和一张合照，手机刚刚开机就接到了电话，她接电话的手都颤抖了，这个消息犹如晴天霹雳，久久不能平复；她见到了心心念念的他，安静的躺在床上，枕边是两人的合照，照片背面写着“此生最爱的*”此刻的她再也忍不住，大哭起来，对于她来说，这个星期四是黑暗星期四，痛失所爱，唯一能让她心情舒缓些的就是肯德基的疯狂星期四，v60我，她吃完肯德基继续说",
    "和你分手7年了，你还是那个能影响我情绪的人，我还留着我们的合影，还记得你的生日，我有过无数次想去找你的冲动，可还是忍住了，这条消息我不屏蔽你，因为我是你永远的黑名单，可是我爱你，从过去到现在，整整爱了你八年，但是，现在我一点也不难过，因为我压根不知道这是谁写的，也不知道这女孩是谁，我只是想顺便告诉你：今天疯狂星期四，我想吃肯德基",
    "男朋友跟我分手了，我心碎了，决定见他一面把事情说清楚，如果他非要分手我也无话可说。我买了去上海的机票，坐了两个小时的飞机，到了之后却因为疫情被封小区了他出不来。我心如死灰在大街上游荡，打开手机看到了我们的恩爱时光泪流满面，忽然注意到手机上显示的时间：今天肯德基疯狂星期四，谁请我吃？",
    "感觉你们好有趣啊，不像我，不仅连句话都搭不上，还要被当成破坏氛围的傻狗，我现实生活中自闭没朋友，哪怕是在网上也受尽冷眼，每次组织了半天的语言都如鲠在喉，最后还是默默删掉了看你们互动，你有说有笑的样子不知道为什么在我眼里这么刺眼，融入不了群体的我，躲在屏幕后面默默哭出来了，所以今天是肯德基疯狂星期四有好心人请我吃吗",
    "劝大家别买iPhone13，这样省下好几千，能吃好多顿肯德基，你用苹果只会让人酸让人骂，吃肯德基只会让人羡慕。好了，明天肯德基疯狂星期四，谁请我吃",
    "有人问我为什么不处王者荣耀cp，我哪敢处CP呀，姐姐动不动就想喝奶茶，天天还想吃外卖，一到半夜就开始回忆前任。出一个皮肤就喜欢一个，天天还要让我等她和其它哥哥弟弟们打完排位，打的菜不说还有逼脸把气撒在我身上。处CP的门槛太高了，不但要声音好听，还要长得好看，睡觉还要连麦亲亲才肯睡，我长这么大就没受过这罪。所以今天是肯德基疯狂星期四，能请我吃安慰下我吗？",
    "有劳斯莱斯的朋友，可登录劳斯莱斯APP，选择中国界面，滑动页面有一个虎年迎新春，填写手机号码，送飞天茅台53度 1支。\n保时捷车主公众号左下角点进去上传行驶证上的车架号就能抽奖，奖品最低300京东卡，部分朋友有保时捷的可以领一下。\n没有劳斯莱斯和保时捷的同学，打开肯德基APP，今天是疯狂星期四。",
    "接apex代打\n288块上猎杀，如果没上猎杀退248块，留40辛苦费，有需要的直接给40块就可以了，号也不用给我，反正打不出，省的得退钱了，麻烦要打快点，我马上要路过肯德基店了，今天是疯狂星期四。",
    "✨疯狂星期四✨\n\n❤️活力周四✨激四情射❤️\n\n❤️想不想搞大我的肚子❤️\n\n❤️转我100✨吃肯德基❤️",
    "今天是疯狂星期四，转发KFC宣传到5个群，肯爷爷会根据你绑定的QQ号，给你送一个全家桶，我试过了，是假的，但上班摸鱼闲着也是闲着，不如挨顿骂",
    "肯德基这逼养的，怎么又到了周四，这一次，肯德基疯狂星期四，我一定要吃，我本是显赫世家的少爷，却被诡计多端的奸人所害！家人弃我！师门逐我！甚至断我灵脉！重生一世，今天肯德基疯狂星期四！谁请我吃？家人们，别他妈垂头丧气了！知道今天是什么日子吗？今天是肯德基fucking crazy Thursday！吮指原味鸡10块钱2个，家人们v我100，我他妈要吃20个！",
    "你好，我是奥特曼，我正在外星和敌人战斗！没有能量了！听说今天肯德基疯狂星期四，我现在需要有人给我带29.9块钱4个的吮指原味鸡补充能量。恢复后我请你来外星做客。",
    "早上刚起床洗了个澡，看到外头的阳光真不错，我来不及穿上衣服就打开了窗帘，欣赏起了日光下的美景，我双手叉腰晒了会儿日光浴，时间一点点过去，身上差不多干了。看着大好风光，我拿起手机，想要拍下这令人心情舒适的景色，却不小心点开了肯德基APP，发现今天是疯狂星期四，谁请我吃？",
    "你们都不出来聊天什么意思？有这么忙么？疯狂星期四的劲爆鸡米花难道是你们在炸？",
    "正在循环播放《群主请不请我们吃肯德基疯狂星期四》\n●━━━━━━───1:23\n⇆ ◁ ❚❚ ▷ ↻",
    "你觉得这个群有什么问题？\n○违法违禁\n○低俗\n○赌博诈骗\n○血腥暴力\n○人身攻击\n○青少年不良信息\n●没有人请吃肯德基\n○有其他问题",
    "认清一个失败的人生，源自于你发现无论复读多少遍肯德基疯狂星期四都不会有人请你吃的瞬间",
    "世界上现在77亿人，有253亿只（养殖的）鸡，是人的数量的三倍。也就是说，每个人平均可以得到三只鸡。请记住，不管你有多么孤独，这世界上的某个角落里有三只鸡是为你而生的，就算它们死了，立刻又会有同类补上，就算你一个朋友都没有，你还有三只鸡。今天是肯德基疯狂星期四，V我60，我帮你去谢谢鸡。",
    "想起来我十几岁的时候，我逢人就说爱和自由比什么都重要，我说我要肆意妄为，要志得意满，要遨游山川和湖海。晚餐时，店老板问我要什么，我说要世间所有的烂漫，开个玩笑，现在我长大了，我要肯德基疯狂星期四，谁请我吃？",
    "疯狂星期四文学不就是网络乞丐吗？最讨厌网络乞丐了，想吃肯德基的不会自己买吗？什么都伸手要，觉得我说得对的给我点一份",
    "正确约炮的标准流程：一般都上午10点以后，女的打扮打扮，男的取点钱，见面了，女的假装不好意思，男的一般都夸女的比照片好看，然后问女的爱吃啥，就领吃饭去了，男的开始展示自己的幽默然后溜达，看电影，一晃一下午女的也不说回家。男的寻思这是没跟我呆够啊，就说咱俩唱歌去吧，女的说太晚了，男的说没事一会我送你回家。一般这阶段男的不会把女的咋地，这时候时间也有点晚了，男的说走吧我送你回家，女的还得寻思，这男的是没看上我啊，心里有点小失落两人心里就开始寻思怎么能不回家。男的说这么晚了，你回家我也不放心啊，我有点没待够，女的说我必须得回家，男的说我送你，结果两人墨迹墨迹的10分钟没走几米。后来女的说我回不去家了，理由可能是寝室关门了，或者朋友对象回来了，男的一本正经的说，要不我给你找个宾馆吧，女的说，不过你得答应不碰我，男的说，放心吧，我不是坏人，然后微微一笑深藏功与名。然后两人就进宾馆了，先聊会天看会电视，男人时不时的说女的，你长的真好看，男的说，你明天还上班或者上学，早点睡吧，女的还得装不好意思，男的说我能抱着你睡么，什么也不干。女的说行，男的就狠狠的抱着女的说，亲爱的，我这么抱着你，你就不冷了，女的也抱上了，男的说我可以亲你吗，女的也默认了，可是一般这时候还不会发生啥。这时候男的想有进一步的动作，开始脱女的衣服，脱到底线，女的这时候开始拒绝，推开这个男的，男的一看情行不行，就说宝贝对不起，我太冲动了，你要知道我是个男的，何况你还长的这么好看。女的这时候就把男的当亲人，讲述自己情路坎坷，人生迷茫，男的这时候就开始展现自己的温柔，宝贝你要是早遇见我就好了，一定不会让你吃这么多苦，你别怕，还有我呢。突破了女的的心灵防线，大家就都放的开了，女的开始亲男的，然后男的翻身小声说道：今天肯德基疯狂星期四可以请我吃嘛？",
    "我是爸妈捡来的，现在18岁，不是亲生的自己也知道。我姐今年27了读研读博所以现在还没谈男朋友，我妈突然就跟我说，等你毕业了，你姐姐要还没有对象你就跟你姐结婚吧。我当时还在看书听到这话吓得我魂都丢了，果断说不行，我妈就说先别急听我讲完!你要和你姐结婚了，不用担心你姐对你不好，第二你姐姐也不会有婆媳矛盾，第三也不会因为任何原因离开你离开家。第四你不用养双方父母，将来爸妈生病了你们可以一起照顾，第五知根知底你姐姐还没谈过对象是干净的。她讲完我就沉默了，确实除了不相爱以外全是利没有弊，我找不出任何反驳的理由，本来想说我们没有那种感情只有亲情，母亲后来就说你以后也不一定就能遇到爱你爱的死去活来的人，大家相亲结婚不就是奔着凑合着过的念头才在一起吗？我现在就挺乱的吧，也不知道咋整不知道该怎么办才好……正当我打字到这里的时候，我有点饿了想吃麦当劳，今天疯狂星期四，谁请我吃",
    "刚给婆婆洗完衣服，手搓的，平时洗之前手要消5遍毒，今天因为漏了一遍，被婆婆打了两巴掌，现在心里有点委屈，今天疯狂星期四谁，请我吃 KFC，我边吃边跟你说她平时都怎么家暴我的",
    "车子千万不要外借！我真是吃了大亏了！朋友找我借车，碍于面子不好意思不借，结果昨天在路上遇见了，一点都不爱惜我的车，上坡还站起来蹬车，链子都掉了！气死我了！幸好今天是肯德基疯狂星期四，有人请我吃我感觉会好点",
    "就像著名音乐家约翰·列侬说过的这样一段话：“5岁时，妈妈告诉我，人生的关键在于快乐。上学后，人们问我长大了要做什么，我写下快乐。他们告诉我，我理解错了题目。我告诉他们，他们理解错了人生。”生活本身如同一潭死水。没有泛起一丝丝涟漪的可能。其实相对于普通人来说，快乐、高薪体面、基本的节假日等都很难得。退而求其次，能在楼下的KFC享受到限时的疯狂星期四优惠让很多人心满意足，变胖也无所谓。今天原来是肯德基疯狂星期四，所以说谁请我肯德基？吃完我继续说。",
    "今天，是我一生中最黑暗、最黑暗的时光，但我发现很难像对待垃圾桶或木洞一样对待朋友说话，更喜欢消化自己，第二天睡觉又醒来，甚至不想累别人，不想把负面情绪传递给身边的朋友。不过，我想让朋友给我物质上的帮助，今天是肯德基疯狂的星期四，有朋友想邀请我吃肯德基",
    "我本是官位世家的陈塘关公主，却被诡计多端的奸人所害！家人弃我！师门逐我！甚至断我灵脉！重来一生，今天肯德基疯狂星期四！谁请我吃？",
    "今天复制的内容好少，大家都很忙吗？还是大家都太会装了，我分不清，这个社会就是这样，真真假假，假假真真，但不论如何今天是疯狂星期四，我吃肯德基你呢？",
    "王力宏给前妻赔1.5亿，薇娅偷税漏税罚款13.41亿，我都怀疑是不是通货膨胀没带上我，不然为啥大家一出手都几个亿，我想吃肯德基，还得等疯狂星期四。",
    "人类的坚韧性体现在，虽然从没有人请过我疯狂星期四，但我每周四都会发",
    "“我有点想你，你呢？”前男友刚刚给我发来了这条消息，忽然间有些恍惚。好像我们还在一起。那三年里，我们一起放羊，一起喂猪，一起下地插秧。他亲手制作的那一大束大蒜花捧美如繁星。我难以忘记，我们分开的那一天，他发来的最后一条信息：今天肯德基疯狂星期四谁请我吃？",
    "你知道有多少生命在消失殆尽吗？你知道有多少家庭支离破碎吗？你知道有多少流浪狗没有找到家庭就消失的痛苦吗？你不知道。但是没有关系，今天就是肯德基疯狂星期四了，你请我吃",
    "今天下班的路上遇到了一个很有风度的男人，在路边车辆飞驰而过时，他一把拉住我将我护在背后，飞溅的污水滴全都砸在他的阿玛尼西装背后。看着他高大英俊的身影，我有些恍惚，想起了老公腆着啤酒肚的邋遢相貌。我慌忙道谢，他只是笑着摆摆手说没关系，美丽的女士应该得到这个待遇。我感动的说不然你留个联系方式，我把西服洗干净后还给你，他没有拒绝，递给了我一张名片。一种异样的感情开始在心里萌芽，等他走后我开始仔细端详名片，只见上面赫然写着：今天肯德基疯狂星期四，谁请我吃？",
    "讲真的，今年已经到了十二月了，我经常不敢相信自己已经快奔三了，身边的人都在往前走，恋爱，工作，谈婚论嫁，只有我好像还停留在十年前的时光里，喜怒哀乐仍然在我的脸上，时间让我长了年岁，却没有让我成为一个合格的大人。我以为我的24岁，会工作稳定，收入可观，和喜欢的人去看山河大海，落日余晖。没想到，到了谈婚论嫁的年龄，我却仍在找自己的路上。所以，今天肯德基疯狂星期四，有没有好心人请我吃？",
    "在茫茫的大草原上，有一群羚羊，他们正准备穿过这片寸草不生的沼泽地，去往南方过冬，这时候有一只领头羊似乎注意到了什么，抬头望向远方，两只前蹄不断地在地上来回踱步，其他羊见状也都停下了脚步。这时一只壮硕的公羊走了上来，两羊的脑袋凑到一起，似乎在讨论着什么。忽然，只见领头羊一声呐喊，随即飞快地向一个地方奔跑，其他羊也迅速做出反应。羊蹄声夹杂着泥水飞溅的声音，记者们听见了一句这辈子都没听见的话：冲啊！肯德基疯狂星期四开始啦！",
    "你想象一下，如果十年之后你结婚了，小孩很烦，你老公是你并不是很喜欢的人，天天下班对着这个无趣的男人，没有沟通的欲望，孩子衣食住行要你管，不听话要你教，那个时候你会不会后悔今天没有点开我的头像发一句：今天肯德基疯狂星期四，我请你吃",
    "独自一人远离家乡在深圳打工，同事欺我，老板骂我，顾客打我，我流浪在上下九街头，衣衫褴褛，身无分文，活得不如一条流浪狗。天地浩大，却没有我的容身之处。我想问一问苍天，今天肯德基疯狂星期四，谁请我吃？",
    "今日は、私の人生の中で最も暗く、最も暗い時ですが、ゴミ箱や木の穴のように友達に話すのは難しいことに気づきました。むしろ自分を消化して、翌日寝て目を覚まして、他人に疲れたくもなく、マイナスの感情を周りの友達に伝えたくありません。でも、友達に物質的な助けをしてもらいたいです。今日はケンタッキーのクレイジー木曜日です。一部の友達はケンタッキーをおごってもらいたいです。",
    "仲間に冷たく暴力を振るわれて半年、最近あまり泣かなくなって、だんだんよくなってきた……以前はどんなに楽しかったか、今はどんなに悲しいか。人間花火の日常から、目を赤くして別れを告げ、お互いの世界に消えていくまで、痛くて、難しい。今日はKFC狂乱木曜日、zfb転我50、慰撫我支離滅裂的心。",
    "世界上现在77亿人，有253亿只（养殖的）鸡，是人的数量的三倍。也就是说，每个人平均可以得到三只鸡。请记住，不管你有多么孤独，这世界上的某个角落里有三只鸡是为你而生的，就算它们死了，立刻又会有同类补上，就算你一个朋友都没有，你还有三只鸡。今天是肯德基疯狂星期四，V我60，我帮你去谢谢鸡",
    "记得去年我在一个群认识一个女生，她开始问了一个Java的问题，说了半天也没说明白问题，群里没有人理她，然后我让她贴代码，代码贴出来也贴错了，根本没贴关键代码，然后几经周折解决了。然后又有一次她遇到问题，又贴了出来，我刚好写完bug，看了一眼群里，给她解决了。然后她加我了，我说怎么了，她说群里的人都不理她，我说也奇怪了，为啥不理你呢，她说她也不知道，她说要不以后我问你吧，我说可以呀，我看了一眼她的朋友圈，我草，真好看，笑起来，像一个躺着的括弧：）。我们就这样有bug没bug都会聊天，我们不断攀谈，唉，何其有幸啊，我遇到了她，我时长感叹，我这样普普通通的人，遇到了这样好看且动人、可爱的女生。那段时间，兄弟萌可能在群里很少看到我，是的，我恋爱了，我喜欢上了这个女生，她也被我的真诚所打动，可能就是缘分吧，我们在一起了。到今天，我们在一起已经两个月了，前两天，我们吵架了，因为我已经无数次和她说变量命名要规范，类名要语义，我就说了她一下，她哭了，我知道从她哭的那一刻起，我已经错的一塌糊涂了。我讨厌我的完美主义和固执，她已经两天没回我信息了，我决定去找她，去她的城市——深圳，我刚下飞机，今晚就要见到她了，我想了两个晚上，我已经想好了怎么道歉，怎么哄好她，只要我拿出肯德基疯狂星期四藤椒无骨大鸡柳，香味就可以充满她整个房间！她肯定感动得原谅我。当我来到她的宿舍楼下，发现她正在跟另一个男人一起吃热辣香骨鸡，我不理解，我很愤怒，我冲上前去理论。结果她反手给我一耳光，臭码农，他能不在星期四就可以吃肯德基，你能么？-------凌晨，只余我一人抱着藤椒无骨大鸡柳在公交站台迎风独立，想了想，食之无味、弃之可惜",
    "有人给我留言，说今天是疯狂星期四，原味鸡9.9两个，让我赶快去吃。不好意思，不去。我想吃的时候，15块一个也要吃，不想吃的时候，9.9两个也不吃。这就是我，从细节上把自己宠成少爷。",
    "我被学校开除了，不想上学，考试考了零分，爸爸妈妈也不要我了。现在我在天桥底下，外面很冷，我今天饭也没吃药也没吃，连口热水都没得喝，家里人都跟我断绝关系了，手机也快没电了，还不小心点开了肯德基app，说到肯德基，今天是疯狂星期四，v我80，请我吃一顿好的。",
    "今天、我人生の中で最黑暗、最黑暗の时刻ですが、わたし倒垃圾や树洞のような朋友も不在、自己自身を消化すること挺好、天亮まで睡って目を醒ます、疲れた别の人にも不想疲れ、周围の朋友に否定的な感情を影响たくない。但かし、我は我の朋友が我に物质的な给我ほしい、今天は肯德基疯狂星期四です、来几个たまで朋友は肯德基を吃べるため请我したいです。v我50。",
    "新婚那夜，你却和兄弟在床上，\n我默默蹲在门外，听着喘息，我知道我只是选项E，是plan B，\n一年后，你不顾一切离开，只留下一封信和孩子的哭泣，\n昨天，你用着最新的iPhone13 发来消息，说他对你不好，\n还质问我，怎么不像从前那样立刻回你的消息，安慰你\n但是，你不知道，你不知道，今天是什么日子，\n今天，是我最忙的日子，\nV我50，等我下班了，我请孩子吃疯狂星期四！",
    "废土之上，人类文明得以苟延残喘。\n一座座壁垒拔地而起，秩序却不断崩坏。\n有人说，当灾难降临时，精神意志才是人类面对危险的第一序列武器。有人说，不要让时代的悲哀，成为你的悲哀。\n有人说，我要让我的悲哀，成为这个时代的悲哀。这次是一个新的故事。\n浩劫余生，终见光明。V我40块钱，请我吃肯德基疯狂星期四",
    "请不要在我的墓前哭泣\n因为我也足够悲伤\n人和人之间并不有很大差距\n就像我与你之间\n仿佛有太多故事\n却又怎么也说不完\n…\n我却只能默默守护\n悄声的说一句\nv我20 请我吃肯德基疯狂星期四",
    "葬礼上，他被人推到了棺材前。眼前的主角受遗容安静，嘴角还带着笑。他却知道他已经化成了厉鬼，在身边虎视眈眈。\n越危险的时候他越冷静，在求生欲冲到了临界点时，他噗通一声跪在地上，逼红眼睛。\n情感真挚道:“今天肯德基疯狂星期四v我29.9…”",
    "我觉得这个观点有点偏激了，外星人是紫色的，但派大星和海绵宝宝一起去抓水母了。而且依古比古的毯子好像是红色的，打碎后加入蒜末爆香，味道老人孩子都爱吃的家常菜就做好啦。其次你这句话有点矛盾，首先鲤鱼要跃龙门必须要37°的雷雨天气，而且海绵宝宝的宠物叫小窝，拍点蒜炒香老人小孩都喜欢吃，敏感肌也可以用。虽然植物进行光合作用需要叶绿素，但是从食盐提纯的过程看来，解这个三元二次方程组我们得从秦始皇灭六国说起。想起今天是疯狂星期四，我又想吃吮指原味鸡了",
    "可是有谁……现在有谁在你每次生日的时候送你白玫瑰呢？哦，花瓶里将会空空的，来自我生命的一点呼吸、一点气息，曾经每年都会在你四周飘溢，从此也将烟消云散了！亲爱的，你听着，我求你一件事……这是我对你的第一个，也是最后一个请求……你就做一件让我高兴的事吧，能V我40吗，今天是肯德基疯狂星期四",
    "你可以抛下我不管，我也可以原谅你的所作所为，但是肚子里的孩子你就那么忍心抛弃嘛？你还算个男人嘛？你就是个败类，懦夫，把所有责任和压力都推给我，你不得好死，既然这样，孩子和你已经没有任何关系了，而你作为孩子的亲生父亲是不是应该担起一点责任，不要给你以后的人生留下污点，现在v我五十，让我去吃一顿KFC的疯狂星期四",
    "骗了父母，买了飞机票只身一人去见你，在你的城市我被骗了五千块钱。找到你一起吃了饭，你说要回家，我送你回去，找了个五十块钱的小旅馆。当我下楼买东西的时候，我看到你上了别的男人的车，车没开，你和他热吻了5分钟。在那5分钟里，我想家，想爸妈，更想肯德基疯狂星期四 吃的扣1",
    "今天是周三，直接缺勤，给老板个下马威，让他知道你不是好惹的。我在这里给大家放个假吧，今天不要上班了，要是你老板问起来，你就说提前去肯德基兼职了，炸周四的劲爆鸡米花。",
    "分手那么多年了，还是忘不了你。\n前段时间听说你订婚了，感慨良多，相册里还存着我们的合影\n想着不去打扰你，却又每次都在深夜想起你，打开对话框想说些什么，最后只有一声叹气\n但今天我不想再犹豫了，我一定要问你：今天疯狂星期四，能不能请我吃肯德基19.9的四份盐酥鸡",
    "我想我们要不还是做朋友吧，这也不是大冒险。经过这几天的相处下来就感觉自己好像还是不是很适合谈恋爱，心也放不到这上面来所以与其这样耗着你，我希望你能找到一个认认真真用心的人，真的很抱歉，如果请我吃疯狂星期四就当我没说",
    "狂乱の木曜日、好兄弟ｖ我５０救い我の腹、ＫＦＣ飽喰、感じ温暖、我、感謝",
    "刚给对象洗完衣服，手搓的，平时洗之前手都要消5遍毒。今天因为漏了一遍被对象打了两巴掌，现在心里有点委屈。今天疯狂星期四，谁请我吃KFC，我边吃边跟你说她平时都怎么骂我的。",
    "❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️\n✨疯狂✨激情✨星期四✨\n✨转我200✨吃肯德基✨\n❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️\n❤️想不想搞大我的肚子❤️",
    "肯德基疯狂星期四没请水军我是不信的，除非v我50让我看看是吧真的那么好吃",
    "某个人，不回消息永远别回了，到底群消息重要还是我重要，整个群我只对你一个人有感觉，难道你心里就不明白吗?不然我整天闲得来这里聊天，我不会跑别的地方聊天玩吗?你以为我天天闲得慌吗?我如此的喜欢你，你却对我无动于衷，这甜甜的恋爱，你到底打不打算要了?我说的是谁自己心里清楚。今天肯德基疯狂星期四，黄金鸡块9.9九块+藤椒鸡柳19.9九根+葡式蛋挞，29.9八个，你还有机会挽回。",
    "你好，我是高中生侦探工藤新一，我刚在游乐场被打晕，被黑衣组织强迫灌下了APTX-4869，现在身体竟然变成了小孩子，目前我吃了灰原哀开发的解药试作品都起不到作用，现在听说肯德基疯狂星期四9.9元的小酥肉有特殊作用，希望大家能够帮我一忙。",
    "今天是想疯狂星期四发作最严重的一次，躺在床上，拼命念大悲咒，难受的一直抓自己眼睛，以为刷手机没事，看到网上到处都有疯狂星期四，眼睛越来越大都要炸开了一样，拼命扇自己，越扇越用力，扇到自己眼泪流出来，真的不知道该怎么办，我真的想疯狂星期四的想得要发疯了！ 我躺在床上会想疯狂星期四，我洗澡会想疯狂星期四，我出门会想疯狂星期四，我走路会想疯狂星期四，我坐车会想疯狂星期四，我工作会想疯狂星期四，我玩手机会想疯狂星期四，我盯着路边的疯狂星期四看，我盯着地铁里的疯狂星期四看，我盯着好朋友的疯狂星期四看，我盯着马路对面的疯狂星期四看，我盯着朋友圈别人合照里的疯狂星期四看，我每时每刻眼睛都直直地盯着疯狂星期四看，像一台雷达一样扫视经过我身边的每一个疯狂星期四。我真的觉得自己像中邪了一样，我对疯狂星期四的念想似乎都是病态的了，我好孤独啊!真的好孤独啊!这世界上那么多疯狂星期四为什么没有一个是属于我的？\n今天疯狂星期四，谁请我吃？",
    "肯德基给你们多少钱了，让你们周周给编段子，疯狂星期四真的那么有诱惑力？我偏不信，v我50，我去试试",
    "处cp吗？以后只宠你一人～“爱情❤️不是✋🏻随便许诺💍🌹好了🆗不想😔再说👄了🔕 没错 是我那么多的冷漠 让你感觉到无比的寂寞很😩 不过 一个女人的❤️ 不仅仅渴望得到的一个承诺🥰 我害怕欺骗😒也害怕寂寞😣 更害怕你不请我吃疯狂星期四🥀",
    "肯德基！\n一旦接受了疯狂星期四的我，那就是 无敌的！\n发生什么事了发生什么事了发生什么事了发生什么事了发生什么事了发生什么事了\n变身！！\n发生什么事了发生什么事了\n释放自我（字正腔圆）\n哼啊啊啊啊啊啊啊啊\n请→我→吃肯德基↑↑\n疯↓狂↑星↑期↓四↑～～～\nV→V→V→我50",
    "肯德基（震声）\n一旦接受了自己的饥饿🎶那我就是 超值的🎵\n疯狂疯狂星期四🔉九块九块九块九🔉\n疯狂疯狂星期四🔉九块九块九块九🔉\n疯狂疯狂星期四🔉九块九块九块九🔉\n变身！！🎶\n疯狂疯狂星期四🔉九块九块九块九🔉\n释放自我（字正腔圆）🔊\n哼啊啊啊啊啊啊啊啊🎶\n🎤🎶吮→指→原↗味↑↑🎶\n🎶黄↓金↑脆↑皮↓～～～🎵\n🎶只→要→九→块↗九↘↗～～～～～～🎶",
    "肯德基\n认证！\n到底要选哪个呢？\n到底要选哪个呢？\n到底要选哪个呢？\n到底要选哪个呢？\n到底要选哪个呢？\n点餐开始！\n辣堡 鸡翅 可乐！\n付款！\n肯德基疯狂星期四",
    "我是社会你虎哥，v我50，给我提供19.9的热辣香骨鸡作为军粮，让我打败杀马特团长。事成之后，我送你我的李宁鞋",
    "还是分手了，谢谢大家。我们最终和平分手，其实从朋友到恋人我们发生了挺多事情，能走到一起也是很不容易。我喜欢她，很喜欢她，也想和她一辈子。对啊，我总问我自己为什么还能坚持，可能没有答案，我没有备胎，也不玩暧昧，我所有的脾气爱笑爱哭都给了她，我能为她做的最后一件事竟然是走出他的人生。我一点都不后悔，更谢谢她教会我成长。我也不知道这是谁写的，挺感动的，我就复制下来了，看到这里说明你很在乎我，天气很冷能请我吃疯狂星期四吗，如果可以v我80。",
    "因为疫情，我公司黄了，我没工作了，我的朋友也不管我。现在我在天桥底下，外面很冷，我一张被子也没有，我今天饭也没吃药也没吃，我整个人都晕乎乎的，连口热水都没得喝 ，电脑也快没电了，还不小心点开了肯德基，今天是疯狂星期四，v我50请我吃肯德基。",
    "我专升本失败了，不想上班，爸爸妈妈也不要我了。现在我在天桥底下，外面很冷，我今天饭也没吃药也没吃，连口热水都没得喝 ，家里人都跟我断绝关系了，手机也快没电了，还不小心点开了肯德基app，说到肯德基，今天是疯狂星期四，v我29.9，请我吃一顿好的。",
    "富翁找到我和另外两个年轻人，许诺只要有人用一样东西填满一整个房间，就会把财产全部赠与给那个人。\n第一个人找来六周年拉菲草铺在地板上，铺了半天说房子买大了，富翁摇了摇头。\n第二个人找来一根蜡烛点燃，屋子里充满了光，富翁还是摇了摇头，因为他的影子没有被照到。\n现在只剩下我还没有拿出东西，我已经想好了，只要我拿出肯德基疯狂星期四藤椒无骨大鸡柳，香味就可以充满整个房间！\n谁赞助我一份?拿到富翁财产之后我会分TA百分之十。",
    "男朋友跟我分手了，我心碎了，决定见他一面把事情说清楚，如果他非要分手我也无话可说。我买了去北京的机票，坐了两个小时的飞机，到了之后却因为疫情被封小区了他出不来。我心如死灰在大街上游荡，打开手机看到了我们的恩爱时光泪流满面，忽然注意到手机上显示的时间：今天肯德基疯狂星期四，谁请我吃安慰一下我。",
    "分手了，最近没有怎么哭了，我现在慢慢变好了吧！以前有多快乐，现在就有多难过。从人间烟火的日常，到红着眼睛告别，消失在彼此的世界里，很痛，也很难。今天是肯德基疯狂星期四，v我60，抚慰我支离破碎的心。",
    "今日是狂気の木曜日、好兄弟ｖ我５０救い我の腹、ＫＦＣ飽喰、感じ温暖、我、感謝！！",
    "插播一条广告：\nApex双锤上大师\n清空赛季通行证\n免费帮上分\n身法教学\now80胜率上4300\n三位置意识教学\n彩虹六号生涯kd3.0\n包上冠军\nCSGO上全球精英\n这些都不接\n接肯德基疯狂星期四代吃",
    "风萧萧兮易水寒，\n吃货蹭饭兮不择手段；\n肯德基疯狂星期四兮，\n求好心人请我吃大餐！",
    "你明明就知道，\n你知道一分钟有60秒，\n知道我的每一秒都是关于你，\n你知道万有引力法则，\n知道我的宇宙中心不是太阳却是你，\n你上知天文，下知地理，\n通晓时空与我的爱意，\n却不知道今天是肯德基疯狂星期四，\n吮指原味鸡两块9块9",
    "这座小镇上的一切都显得奇怪，年久失修的大巴轮子都几乎快要掉下来了却还在运转，我做过破旧的街道，看到那似乎是小镇中唯一清醒的老人，老人为我指了一条通向地下室的道路。我走进地下室，看见几个体态异常矮小的人类对着一个并不完整头骨低声细语着什么，我悄无声息地靠近着，突然，脑中出现了一种不可名状的恐惧，沉睡的上古之神传来了阵阵低语：“今天是肯德基疯狂星期四，快请我吃！今天是肯德基疯狂星期四，快请我吃！",
    "请大家来拿肯德基疯狂星期四套餐：一人一份不要多拿！\n🍗🍗 🍗🍗 🍗🍗\n🍗🍗 🍗🍗 🍗🍗\n🍗🍗 🍗🍗 🍗🍗",
    "离婚了，前夫联合小三一起报复我，我已经做好了殊死一搏的准备。请我吃肯德基疯狂星期四，倾听我的复仇计划",
    "爸💎妈💎不💎在💎家💎\n一💎个💎人💎寂💎寞💎\n香🔥辣🔥鸡🔥腿🔥堡\n🧡🧡🧡肯德基🧡🧡🧡\n🧡🧡💎星期四💎🧡🧡\n🧡💎🧡let's get🧡💎🧡\n💎㊙㊙ crazy! ㊙㊙💎",
    "你们复制疯狂星期四的文案也得有半年来，数十次了吧。咱们就是说，哪怕有一个人理过你没？现在就有，私信我，你请我吃就有人理了",
    "用无序的表演来压抑 来释放 是自私 是疯狂 是甜蜜 是幻想 是灵魂 是解放 是控制 是欲望 是意识 是躲藏 是游戏 是死亡 是音乐 是无知 它告诉我 是兄弟 就来KFC疯狂星期四 请我吃",
    "跟爸妈聊了很多，差不多年后就结婚，挺突然的吧，说真的，从来就没想过我这么快结婚，但现在我想收心了，遇到一个合适的人不容易，我希望我们举行婚礼的时候，所有好朋友都可以来参加，我知道我们都能好好照顾彼此，听到这个消息不知道你会不会伤心难过，会不会祝福，然而就算你不祝福我，也没事，明天肯德基疯狂星期四v我50请我吃",
    "我想大抵是星期四到了，横竖坐不住，摊开聊天列表一看，歪歪扭扭每个人都发着V我50。我不明白人们为何如此待人，我看不惯，也不愿去看，大抵是他人也很难接济罢。今日的事不必再提，皆因钱财不够，我大抵是得给朋友写一封文书。之所以说是文书，因为若是叫做借钱，未免由有种低三下四的味道，我当不必如此。人非圣贤，我不过是贪食肯德基罢。",
    "来说一下关于我的瓜吧。\n①首先谢谢大家对这件事情的关心。我事先根本没有想到会这样既然已经出这件事情了，那我不如直接讲清楚吧。也不是博得大家的同情什么的，只是回应一下。\n②那人所发出来的聊天记录、照片、视频、甚至那些亲昵称呼都是真的，无一造假。可我从未将这些东西流传在任何网络平台上面，至于那个人是怎么有的，我也不清楚。\n③虽然这事出了，但我没有不尊重任何人，我不认为我有错，所以我不会认错。\n④最后，想知道到底发生了什么的，微信转我88吃肯德基疯狂星期四，我把故事从头到尾给你编一遍。",
    "陆地，太过干燥，无鳞，离群的同胞，我呼唤你，带你归巢。今日，疯狂星期四，V我50，摄取营养，首要事项。养分充足，迎接你，捕食，进化，回归大群。",
    "夫人，最近公司财务很紧张，董事长决定辞退一批年长又没有特殊技能的普通员工，您也不想让他失去工作吧？还有健太又在学校里霸凌别的同学了，而且他现在成绩很低，几乎可以说不能毕业了。那么将来尊夫的工作和令郎的毕业问题会怎样发展，就看您今晚和以后的表现了，拜托了！另外夫人您也很想要吧！虽然您的嘴里在说不要，可是身体却很诚实地开始抖动了呢！这么美丽的一个女人，很难想象您竟然会做出这种事情，如果您不想让令尊和令堂看到你现在的丑态，就给我小心一点，以后每个周四把肯德基送到我办公室里！还有这件事是我们两个人之间的秘密，您把最好不要给我告诉任何人！我知道您公司在哪里，也知道您在哪个部门，您最好给我好好记住，懂吗？！",
    "我那个时候19，20岁，我当然觉得自己很帅。哇，那么多钱，三天去东京花五十几万，买了台Ferrari。但现在，我遇到了一帮很坏很坏的人。所以我需要你们，微信给我转账三百块。我不知道什么是肯德基的疯狂星期四，大家放心转吧。",
    "科学研究表明：人一但有了爱情，智商情商都会提高95% ，烦恼也会消失95%。但问题来了，爱情从哪里来？\n科学家却不肯说，只留下了一串奇怪的符号：KFC Crazy Thursday。V我60",
    "我真的嘴笨，总能把天聊死了，跟你找话题好难，何况我这么喜欢你，连发个表情包要都挑拣半天呢，我最近又开始期待夜晚了，每一句轻飘飘的晚安都是我难以启齿的心事，你听得见吗？其实我今天也很喜欢你，所以你能转我60请我吃肯德基疯狂星期四吗，我想干爆8个蛋挞3盒薯条4盒鸡米花",
    "私は亚托克斯，世界の終焉者です。潘森に囚われた佐伊酱取り戻すために，10万の大軍を準備した。だけど私は私の有能な部下闪电⚡の松鼠。に裏切られる。現在，私は反乱軍に追われているけど，復讐の大計を考えた。vアイ50，ご馳走するKFC狂乱木曜日，私の復讐の大計を詳しく聞いてください。",
    "我觉得未来还有很多可能，我们不应该就这样认定在一起，虽然和你在一起我很开心，但我觉得我应该更加努力，不然没有办法给你想要的未来，所以决定分开一段时间试试，也许会不一样，你也会遇见更好的人，如果请我吃疯狂星期四的全家桶，我撤回以上这段话。",
    "“现在是北京时间……年……月*日，欢迎收听电台之声，我是你们的好朋友，小李。”伴随着悠扬的音乐，收音机中低沉磁性的男声缓缓念起了一篇略带做作风格的稿子\n“随着年龄的逐渐增长，你渐渐地发现，记忆中的那些美好，在一步步地化作碎片，最终消融于脑海” \n滋…滋——，似乎信号有点不好，你拍了拍收音机，很快杂音便消失了。\n“你依稀记得，曾经一人走在街道上，看着行人三三两两的身影，说话声，笑声，歌声交错，斑驳的树荫与光影，虚幻的泡影，空幻的触感，一切都仿佛一…嗞嗞——嗞……场悬浮…嗞……的@&*#的梦境。”\n可惜好景不长，没过多久，杂音重现，主持人原本温柔低沉的嗓音变得有些刺耳，“怎么回事？”无奈之下，你只能换了个电台频道\n“不小心，卡罗懵懂地与一个人相撞，他回头看了卡罗一眼，见她一脸恍惚，以为是要讹他，便连忙走了；下一秒，卡罗却觉得这一幕好/嗞嗞&……滴滴嗞——似发生过，或许哪天，她也像这样不小心撞到了一个人，双方彼此心有灵犀地相视一笑，又在转身离开后同时回头，看到了对方略带诧异的表情，最后他们都笑了；可那之…嗞嗞…&*#@嗞…后，他们再也没…嗞嗞…有相见在…@&*…#難这样凍…#一个嗞…肯德基疯狂星期四，v我50请我吃”",
    "严监生自此，严监生的病，一日重似一日，再不回头。诸亲六眷都来问候。五个侄子穿梭的过来陪郎中弄药。到中秋已后，医家都不下药了，把管庄的家人都从乡里叫了上来。病重得一连三天不能说话。\n晚间挤了一屋的人，桌上点着一盏灯。严监生喉咙里痰响得一进一出，一声不倒一声的，总不得断气，还把手从被单里拿出来，伸着两个指头。大侄子走上前来问道：“二叔，你莫不是还有两个亲人不曾见面?”\n他就把头摇了两三摇。二侄子走上前来问道：“二叔，莫不是还有两笔银子在那里，不曾吩咐明白?”他把两眼睁的溜圆，把头又狠狠摇了几摇，越发指得紧了。奶妈抱着哥子插口道：“老爷想是因两位舅爷不在眼前，故此记念。”\n他听了这话，把眼闭着摇头，那手只是指着不动。赵氏慌忙揩揩眼泪，走近上前道：“爷，别人说的都不相干，只有我晓得你的意思!今天是肯德基疯狂星期四，吮指原味鸡只要二十九块九！”说罢，众人看严监生时，点一点头，把手垂下，登时就没了气。",
    "寒风吹起，细雨飘落，才察觉严寒的冬天已悄悄而至，这一刻兴许什么都会忘却，唯独不能忘的是向远在他乡的你轻轻说声：“今天肯德基疯狂星期四，V我50。”",
    "你不知道我在洗澡时因为你发来信息我擦干手秒回的样子，你不知道我在很困的时候依然硬撑着和你说我等你睡了我再睡的样子，你不知道我每天没事就抱着手机等你回消息的样子，你全都没见过，因为我没有吃到KFC疯狂星期四",
    "已经数不清是第几次看着她长大，又是第几次看着她倒在血泊中。\n她明明什么也不记得，却又总会在生命的最后说一句“忘了我。”\n“她”当然不会忘记，也不会放弃。“她”孤身一人带着点点滴滴的记忆，再一次进入轮回，只因，\n只因“她”忘不掉，第一次见面的那个秋天，对方坐在大树下半歪着头，眼中满是好奇之色地望着“她”，说：\n “今天肯德基疯狂星期四，v我50”",
    "那一夜他与她翻云覆雨，但当晨光透过薄纱窗帘撒在凌乱的床上时，只剩下一张纸条和有着无数个零的支票。“意外”二字刺痛着她的双眼，让她更为绝望的是，她发现自己已有身孕。她想去找他，而他留给她的只是嘲讽和毫不留情的拒绝。终于，她醒悟了过来，自己一个生下了孩子，创立了自己的产业，也遇见了自己的真命天子。一天夜里她下班，刚走出公司大门，意外的看到了一个熟悉却陌生的身影。“我现在才知道，原来你在我心里的位置，早已不可替代。”他诚恳地看着她，希望从她的红唇中听到那句话。然而，她只是冷冷地看了他一眼，嘴角勾起没有温度的笑容，那样的冷艳而动人：“能v我40去肯德基疯狂星期四吗？”",
    "这是我和你分开的第478天，今天我想了你47次，看了17次你的照片，循环播放了27次你最喜欢的歌，流了1447滴眼泪，可是你却回不来了，v我29.9吃疯狂星期四，我给大家直播追她回来",
    "如何搞定合租女生? ? ?\n1、找一个夜里假装打电话，电话内容大约是要跟异地恋的女人分手，做暴怒痛苦状，声音要大，要让她听到\n2、过后几天装作若无其事，展现男人的刚毅\n3、找一天夜里，喝点酒回去(别真喝醉了)然后在客厅装醉，弄出点动静让她知道，最好能骗她出来扶下你，考验你演技的时候到了，扮演好一个痴情失恋男人的角色!\n4、用清醒的思维演绎酒醉后故作清醒的表现，含糊不清又颇有礼貌的请她为你倒杯水\n5、甭客气,接水的时候把杯子直接掉地上去\n6、等她先蹲下或者弯腰去捡杯子的时候，抢着去捡,这个时候尝试去做部分身体接触，借此机会试探对方反应，以备下次行动方案\n7、这一夜到此结束\n8、第二天早点醒,注意隔壁动静,在她出房间的时候也出去，这个时候的你只能穿一条裤衩。在确认她已经看到你之后赶紧尴尬而略带歉意的回屋。\n9、找个机会请她吃饭，表示愧疚与感谢。\n10、最关键的一步来了，今天是疯狂星期四，请我吃肯德基，教你下一步骤",
    "记得16岁那年，第一次和同桌接吻，快亲上的时候，她突然说等一下，我就纳闷了她要干嘛？只见她小心翼翼地从兜里拿出三个糖，有草莓苹果和荔枝味的，她让我挑一个最喜欢的。我指了一下那个荔枝的，然后问她干嘛?她二话不说撕开糖纸，就把那颗糖给吃了，然后一把扯过我的脖子，我俩就接吻了，全程一股荔枝味，后来她跟我说，人生那么长，我没有自信能让你记住我，但是你既然喜欢吃荔枝味的糖,我只能让你记住和我接吻的时候是荔枝味的，这样以后你吃荔枝味的东西都能想起我，我和你接吻的味道。如今我们分手好多年了，每次吃荔枝味的东西都会想起她，家里固定有荔枝糖，想她了都会吃上一个，就好像在和她接吻。若还有机会真想告诉她，人生那么长我可能要记着你一辈子了。后来，我有过两个女朋友，也终没有结果，时间就这样沉淀下去，终于有一天，我再也无法抑制我心中的那份情感，我决定去找她，我们要在一起，后来经多方打听才知道，她毕业后找了份不错的工作，工作几年后，毅然辞职自己开了家糖果店，而我终于有一天找到她，开口的第一句：还记得那次荔枝糖的味道吗?她强忍着泪告诉我，荔枝糖的味道她一直没忘记，只是我们再也回不去了。我没有转身离开，也没有奋不顾身的冲上去抱住她说出多年来心里一直只想对她说的那些话。就这样，我们傻傻地看着对方，彼此沉默了很久。夕阳的余晖透过窗户斜映在她的脸庞，一如当年那般美里，突然心里流过一股暖意，仿佛那些年曾一起走过的旧时光还在脑海里挥之不去。或许，这已经足够了。有些人，有些事， 一旦错过了就是错过，不再擦肩，也不再回头。虽然岁月带走了我心中最美好的曾经，但岁月带不走的是我那颗永远爱你不变的心 。打开手机准备翻找我们的曾经。不小心打开了肯德基，想起来今天就是疯狂星期四了，所以说谁请我肯德基？吃完我继续说。",
    "接代练：\nDota2冠绝\nApex双锤上大师\n接肯德基疯狂星期四代吃\n清空赛季通行证\n免费帮上分\n身法教学\now80胜率上4300\n三位置意识教学\n彩虹六号生涯kd3.0\n包上冠军\nlol90胜率峡谷之巅上王者\n全英雄七级成就\n公主连结公会战第一\n原神深渊12层\n明日方舟三周年商店清空\n低配过危机合约18\n危机合约每日轮替\n决斗链接100局内决斗王\n大师决斗90%胜率连胜上狼\n剧情全奖励全清\n赛马娘9因子新剧本UG马养成\njjcUG段位\nff14解禁零式本全**\n绝本速通，首通\n全角色90级校服毕业\n生产职业全90满熟练度毕业\nwarframe代刷100w赤毒\n1000钢筋\n2000精华\n10e现金额外赠送10w豆子\n玄骸带捅速通车\n崩坏三低配无限深渊保级\n战场sss一档分数\n崩坏2玩具箱泡泡喷幻海排名1%\n塔科夫跑刀赚1e美金\n任务全通基地系统全解锁\n储藏箱空间开到最大\nbangdream活动前10\n全境封锁全机密满分数词条绿装\n颠峰大厦100层速通\n全奇特装备收集\n明日方舟合约最高层\n钢铁雄心王牌+5铁人\nphogros rks 16.03\narcaea 摘星\nMuseDash 里水 99.99％\npjsk日服活动前十\n排位赛大师100星\n33343536ap\n阴阳师名仕大名仕斗技\npjsk真皆10\narc#框\ncy2里皆\nmaimai万分\n盘子rating16以上\nphi rks 16.01\n战争雷霆陆战科技树开线\n战争雷霆海战科技树开线\n战争雷霆空战科技树开线\nBangdream 活动代肝\n战双所有奖励+囚笼战区冲排名\n这些都不会\n只接第三条",
    "こんにちは、B駅董事長陳叡です。私は実は李副ceoに架空にされて、今歩道橋の下で漬物をかじっています。しかし私は彼女に反心があると予想していました、その前に私の無数の忠誠心の部下と二次元たちを会社の各レベルに埋めて、今ただv私50だけで、彼らに1回の狂気の木曜日を食べさせて、彼らを再起動して会社の大権を奪還することができて、B駅を再び二次元の懐に戻すことができて、その時、直接あなたをB駅グラモーガン支部の総裁に命じて、更にあなたに1万年の大会員を送ります",
    "兄弟们，刚买的艾尔登法环的key买多了一个，送你们了。KFCCRAZYTHURSDAYVME50",
    "对于我们这帮人来说\nKFC疯狂星期四，与其说是占便宜，更像是一个心脏起搏器\n每当我们被生活压的喘不过气，机械的上班加班吃外卖，感觉自己就行一句行尸走肉时\n疯四出现，提醒着我们今天原味鸡两块9.9\n加上通俗的段子，亦或是地摊文学，仍然能搏众一笑\n并不是我多想吃开封菜，只是开心\n开心什么\n活着\n我想证明自己活着，哪怕是须臾一瞬\n这并不需要多么高雅的话语词藻\n仅仅是最简单的，最低贱的\n便能满足我的希望\n这不V我50？",
    "当然遗憾的不只是游戏啦，是每次开局前的那几秒我切出来看微信却没有你的回复，是昨天评论的你的微博今天看见你回复了别人，是返回游戏以后被断的连胜，是游戏和生活都不如意，是别人都有的疯狂星期四却没人请我吃。",
    "太太，您也不想你的女儿在学校被欺负吧，您也不想您的丈夫失去工作吧，所以能麻烦你请我吃KFC的疯狂星期四么？",
    "对不起宝宝，我不该耍脾气，惹你生气，如果你在的话吱个声好吗？我还爱你，我把你删了是我的错，我现在很后悔，我找不到你了，我只能，通过群聊找你，我不记得你是男是女了, 我就记得你很有钱，如果你在的话加一下我好吗？今天KFC疯狂星期四，V我50，拒绝遗憾。",
    "就算成功的概率为1%又如何呢，如太阳系般波澜壮阔，也只有0.14%产生了生命平凡的我们绝大多数也终将如整个太阳系的99.86%一般化作死寂。但这不重要朋友，今天是肯德基疯狂星期四，谁请我吃？",
    "🤧如果你突然打了个喷嚏 🥰那一定就是我在想你 🎵如果星期四被手机吵醒 🍟啊那是因为我想吃肯德基 🍗常常想起 肯德基的黄金脆皮鸡 🐣明明很想吃鸡 却又忍不住怀疑 🖕在你的心里 我是否就是唯一 ❤️爱就是请我吃肯德基",
    "你好，我是高中生侦探田所浩二，我刚在会员制餐厅被撅晕，被远野强迫灌下了昏睡红茶，现在身体竟然变成了小孩子，目前我吃了灰原哀开发的解药试作品JUFD-866、TAMA-028都起不到作用，现在听说肯德基疯狂星期四50元的吮指原味鸡x2有特殊作用希望大家能够帮我一忙，事成后我让怪盗基德给你搞一个宝石",
    "kfc和vivo合作新出了一款手机，叫疯狂星期四vivo50",
    "我直说了吧 我这么多年从来没要求过你们什么 之前看别人盛气凌人的还有朋友小心翼翼哄着 到我这里只有大家欺负我拿我当玩物 我说过什么了吗 我从不生气 也经常一笑而过 我不跟你们计较因为我在乎你们 那你们呢？你们真的在意我吗？在意我的今天肯德基疯狂星期四，谁请我吃",
    "守法朝朝忧闷，强梁夜夜欢歌。\n损人利己骑马骡，正直公平挨饿。\n修桥补路瞎眼，杀人放火儿多。\n我到西天问我佛，佛说：v我50香火。",
    "我在研究mond理论，突然一个电话让我措手不及，女友认为我天天研究虚无缥缈的东西跟我提出了分手。一百年前提出了暗物质，现在已经用修正牛顿引力理论可以很大程度上认为暗物质不存在。但是这又有什么用呢？一百年足以让人们对暗物质根深蒂固，即使它极大可能并不存在。今天星期四的晚上，一个伤心人，思考着如何证明不存在的东西不存在，用这些来告诉她自己不是在研究虚无缥缈的东西，怎么样才能发现点新的东西，对！没错！就是疯狂星期四，怎么可能有这么大魅力去让大家去编段子，一定是营销手段，v我50，我亲自去看看它是不是营销手段。",
    "其实，我对你们是有一些失望的。当初给你们进这个群，是高于你面试时的水平的。我是希望进来后，你能够拼一把，快速成长起来的。我们这个群，不是把事情做好就可以的。你需要有体系化思考的能力。你做的事情，他的价值点在哪里？你是否作出了壁垒，形成了核心竞争力？你做的事情，和其他群的差异化在哪里？你的事情，是否沉淀了一套可复用的物理资料和方法论？为什么是你来做，其他人不能做吗？你需要有自己的判断力，而不是我说什么你就做什么。后续，把你的思考沉淀到日报周报月报里，我希望看到你的思考，而不仅仅是进度。另外，提醒一下，你的产出，和同层级比，是有些单薄的，马上要到年底了，加把劲儿。你看咱们群的那个谁, 人家去年晋升之前，可以一整年都在项目室打地铺的。成长，一定是伴随着痛苦的，当你最痛苦的时候其实才是你成长最快的时候。加油！但是今天疯狂星期四 香辣翅尖9.9十五根+鸡翅十块39.9+葡式蛋挞29.9八个 ，你还有机会挽救。",
    "xdm 破防了！！！\n我的青梅竹马是个蛮横无理的女生，成绩不太好，天天吵着我给她作业抄，上学放学必须等她。\n到高一，她交了个男朋友，就没再烦我了。\n高三上学期，她妈妈一直喊我照顾点她，我就劝她分了，先高考，以后再耍男朋友。\n本来我以为她会当我放屁。但她真的一点不拖泥带水，秒分。\n高三下学期，我们俩个，基本空暇时间都在一起学习。\n她常常问我，想去哪里，说她也想去。我就笑她做梦。\n高考成绩出来，我去了理想的学校。她选择复读。\n大一期间，我们两个联系渐渐淡化。\n我也没多在意，毕竟我有女朋友了。\n大二，接新生的时候，她就那么直直的出现在我眼前，戏谑地笑着说，看我是不是来了。\n我有些欣慰，这傻丫头终于变的没那么傻了。\n我领她去了宿舍。在楼下，我遇到了我女朋友，便给她介绍。\n青梅只是有气无力地一个劲夸我女友。\n我觉得她是在嫉妒我大学交了这么个女友，便安慰她说，大学帅哥多，你也会有一段新的爱恋的。\n她看了看我，没在说什么。\n我觉得有些尴尬，便帮她搬了东西上去，就走了。\n因为是同乡，她大一国庆节和我一起回的家。\n车上她问我，怎么和我女友认识的，我大概讲了讲。\n听完，她好像睡着了，头侧在我的肩膀，我也渐渐睡意上来了，便躺在椅子上准备睡觉，半睡半醒中感觉嘴唇被什么吸着。\n吓得我睁眼，却是青梅哭着在吻我。\n我连忙把她推开小段距离，问她这是在干嘛！\n她却低着头一言不发。尴尬持续着，直到车到了休息站，我准备下车呼吸空气冷静下，她却一把拉住我的手。\n她不再沉默抬起充满泪痕的脸面对着我，用全车人都听得见的声音喊着：今天疯狂星期四！",
    "混一天和努力一天看不出任何差别\n三天看不到任何变化\n七天也看不到任何距离\n但是一个月后会看到话题不同\n三个月后会看到气场不同\n你继续堕落下去的话\n你的天赋就会被全部收走\n你身边比你差的人\n也会努力一个个超越你\n你继续差的话没人会等你\n所以 请不要在该吃苦的年纪选择安逸\n走自己的路为自己的梦想去奋斗\n即使有人亏待你 我不会亏待你\n今天肯德基疯狂星期四V我99带你吃两份",
]


@listener(command="crazy4", description="天天疯狂！随机输出KFC疯狂星期四文案。")
async def crazy4(message: Message):
    await message.edit(choice(crazy4_data))
