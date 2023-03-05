#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class HotRodSuperSpeedwayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Hot Rod Super Speedway (Original)"
        self._ui_description = "The Hot Rod Super Speedway adds pro difficulty to the short track counterpart. With a length of 59.69m, the speed loving arch is replaced by 4 short straightaways coupled with variable angle turns. Skillful racers may bisect the chicanes to extending speed generating opportunities and pull away from the pack."
        self._ui_length_in_m = 59.69  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "arctic_pro"
        self._track_sector_dividers = [55, 100, 150, 195]
        self._annotations = config.hot_rod_super_speedway_annotations
        self._track_width = 1.066

        self._track_waypoints = [(6.877749443054199, 3.661787509918213), (6.627933979034424, 3.6891591548919678),
                                 (6.378144025802612, 3.716727375984192), (6.1283769607543945, 3.744485855102539),
                                 (5.878616094589233, 3.772302031517029), (5.628854036331177, 3.8001229763031006),
                                 (5.3790905475616455, 3.8279484510421753), (5.129326105117798, 3.8557804822921753),
                                 (4.8795599937438965, 3.8836164474487305), (4.629792928695679, 3.9114575386047363),
                                 (4.380024433135986, 3.9393035173416138), (4.130249977111816, 3.96708345413208),
                                 (3.8804584741592407, 3.9946409463882446), (3.630650520324707, 4.021971583366394),
                                 (3.38082492351532, 4.049073576927185), (3.130981922149658, 4.075949549674988),
                                 (2.8811224699020386, 4.102597594261169), (2.631245970726013, 4.129018068313599),
                                 (2.3813570737838745, 4.1552804708480835), (2.1315314769744873, 4.182417392730713),
                                 (1.881794035434723, 4.2107731103897095), (1.6321449875831604, 4.240346431732178),
                                 (1.3825839757919312, 4.271137475967407), (1.1331110000610352, 4.303147077560425),
                                 (0.8837268054485321, 4.336374521255493), (0.6344304978847504, 4.370819926261902),
                                 (0.3850132077932358, 4.40359103679657), (0.1350918859243393, 4.429395079612732),
                                 (-0.1153416745364666, 4.448118090629578), (-0.36629100143909454, 4.459589004516602),
                                 (-0.6160945892333973, 4.435822486877441), (-0.8587201237678528, 4.371313571929932),
                                 (-1.0874865651130676, 4.26801609992981), (-1.295538306236267, 4.127558469772339),
                                 (-1.4764775037765503, 3.9535964727401733), (-1.62629896402359, 3.7521380186080933),
                                 (-1.745304524898529, 3.530973434448242), (-1.8636749982833862, 3.309363603591919),
                                 (-1.9993194937705994, 3.0978790521621704), (-2.151298940181732, 2.8978124856948853),
                                 (-2.3182089924812317, 2.7100294828414917), (-2.5006580352783203, 2.537310004234314),
                                 (-2.69733202457428, 2.3809815049171448), (-2.9069955348968506, 2.2425865530967712),
                                 (-3.129592537879944, 2.12616503238678), (-3.3631500005722046, 2.0336870551109314),
                                 (-3.605257987976074, 1.966755986213684), (-3.8534475564956665, 1.9281110167503357),
                                 (-4.104434013366699, 1.9182080626487732), (-4.354905605316162, 1.937102496623993),
                                 (-4.60286545753479, 1.9779245257377625), (-4.850281476974487, 2.021980941295624),
                                 (-5.097311973571777, 2.068145513534546), (-5.343934059143066, 2.1164429783821106),
                                 (-5.5903191566467285, 2.1659379601478577), (-5.836361885070801, 2.217108964920044),
                                 (-6.082114219665527, 2.2696584463119507), (-6.327574014663696, 2.3235555291175842),
                                 (-6.572595596313477, 2.379411458969116), (-6.817136526107788, 2.437335431575775),
                                 (-7.0618555545806885, 2.4939935207366943), (-7.311485767364502, 2.521486520767212),
                                 (-7.562535524368286, 2.515997529029846), (-7.809762001037598, 2.4724029898643494),
                                 (-8.045353174209595, 2.3859819769859314), (-8.258959531784058, 2.2544105648994446),
                                 (-8.441039562225342, 2.0817909836769104), (-8.581009864807129, 1.8744714260101318),
                                 (-8.681109428405762, 1.6439650058746338), (-8.781568050384521, 1.4136090278625488),
                                 (-8.882308959960938, 1.183376669883728), (-8.982824325561523, 0.9530460238456726),
                                 (-9.083500385284424, 0.7227852046489716), (-9.184541702270508, 0.49268434941768646),
                                 (-9.285074234008789, 0.26236093789339066), (-9.355420112609863, 0.021814581006765366),
                                 (-9.366334438323975, -0.228639654815197), (-9.301803588867188, -0.47022745013237),
                                 (-9.157926559448242, -0.6746465712785721), (-8.955705165863037, -0.8225192576646805),
                                 (-8.724424362182617, -0.9198991358280182), (-8.480135440826416, -0.9780847281217575),
                                 (-8.230309009552002, -1.0038194358348846), (-7.979228496551514, -0.9980531632900238),
                                 (-7.731260538101196, -0.9585085511207581), (-7.4914939403533936, -0.8839295506477356),
                                 (-7.265609502792358, -0.7743122577667236), (-7.058122396469116, -0.6328902468085289),
                                 (-6.872535467147827, -0.4637025035917759), (-6.692823886871338, -0.2881161905825138),
                                 (-6.492725133895874, -0.13659296929836273),
                                 (-6.2641520500183105, -0.03379184007644653),
                                 (-6.015917778015137, -0.002170264720916748),
                                 (-5.7663774490356445, -0.030724138021469116),
                                 (-5.521281480789185, -0.08565294742584229), (-5.288934946060181, -0.18044884502887726),
                                 (-5.083465099334717, -0.32418685033917427), (-4.912674903869629, -0.5081491991877556),
                                 (-4.782384395599365, -0.7224807590246201), (-4.6636505126953125, -0.9439679384231567),
                                 (-4.538731813430786, -1.162013441324234), (-4.4046748876571655, -1.3745545148849487),
                                 (-4.259946584701538, -1.5799674987792969), (-4.1030250787734985, -1.7762075662612915),
                                 (-3.932309865951538, -1.9605494737625122), (-3.746272921562195, -2.129379451274872),
                                 (-3.543729543685913, -2.277939021587372), (-3.3246184587478638, -2.400669515132904),
                                 (-3.0905004739761353, -2.4914379715919495), (-2.845192074775696, -2.544919013977051),
                                 (-2.594696521759033, -2.5643980503082275), (-2.343833565711975, -2.579355001449585),
                                 (-2.0929625034332275, -2.5941569805145264), (-1.8420894742012024, -2.608939051628113),
                                 (-1.5912105441093445, -2.623616576194763), (-1.3403149843215942, -2.6380040645599365),
                                 (-1.0894079804420471, -2.652198910713196), (-0.8384952545166016, -2.666285514831543),
                                 (-0.5875802934169769, -2.680333971977234), (-0.33666530251502635, -2.6943825483322144),
                                 (-0.08574593998491409, -2.708351492881775), (0.1651745513081586, -2.7223005294799805),
                                 (0.4160903990268665, -2.7363328933715816), (0.6669915318489075, -2.7506260871887207),
                                 (0.9178917407989502, -2.7649329900741577), (1.1688349843025168, -2.778464913368225),
                                 (1.4171209931373596, -2.810842990875244), (1.64935302734375, -2.905639410018921),
                                 (1.8593770265579224, -3.04303240776062), (2.0466140508651733, -3.2103869915008545),
                                 (2.2124545574188232, -3.399070978164673), (2.379397988319397, -3.5868475437164307),
                                 (2.56254243850708, -3.75873601436615), (2.7708990573883057, -3.8985503911972046),
                                 (3.003482460975647, -3.992649555206299), (3.248476028442383, -4.048017978668213),
                                 (3.4964144229888916, -4.089016556739807), (3.7456459999084473, -4.120978116989136),
                                 (3.995734930038452, -4.145682454109192), (4.246043920516968, -4.1680625677108765),
                                 (4.496459007263184, -4.189226984977722), (4.746946811676025, -4.209509611129761),
                                 (4.997488498687744, -4.2291200160980225), (5.248067378997803, -4.248247981071472),
                                 (5.498672962188721, -4.267024993896484), (5.749297142028809, -4.285551428794861),
                                 (5.999933958053589, -4.3039023876190186), (6.250592470169067, -4.321959376335144),
                                 (6.501274824142456, -4.339676380157471), (6.751977920532227, -4.357102990150452),
                                 (7.002697944641113, -4.374282479286194), (7.253431558609009, -4.391266584396362),
                                 (7.504173517227173, -4.408125042915344), (7.75492000579834, -4.42490541934967),
                                 (8.005107879638672, -4.44657301902771), (8.255828380584717, -4.458704948425293),
                                 (8.504947662353516, -4.4280054569244385), (8.743395805358887, -4.3503135442733765),
                                 (8.956387996673584, -4.218177556991577), (9.12837839126587, -4.035868406295776),
                                 (9.251077651977539, -3.817134976387024), (9.327564716339111, -3.578068494796753),
                                 (9.365591526031494, -3.329882025718689), (9.365254402160645, -3.078808546066284),
                                 (9.326939582824707, -2.830678939819336), (9.253893375396729, -2.5904154777526855),
                                 (9.149560928344727, -2.361986994743347), (9.011484146118164, -2.1522310376167297),
                                 (8.84194564819336, -1.9669420719146729), (8.645301342010498, -1.8107309937477112),
                                 (8.42654275894165, -1.6874244809150696), (8.191082954406738, -1.6000699996948242),
                                 (7.9447901248931885, -1.550885021686554), (7.693856954574585, -1.5395675301551819),
                                 (7.442551851272583, -1.5383674502372742), (7.19124698638916, -1.537166953086853),
                                 (6.93994140625, -1.5359660387039185), (6.688687086105347, -1.5355154275894165),
                                 (6.4375269412994385, -1.5364949703216553), (6.186150074005127, -1.5342129468917847),
                                 (5.934433460235596, -1.526841640472412), (5.6823790073394775, -1.5143814384937286),
                                 (5.430981874465942, -1.5118014514446259), (5.181424140930176, -1.5371429920196533),
                                 (4.93126916885376, -1.560838520526886), (4.680135011672974, -1.569189965724945),
                                 (4.429048538208008, -1.559888482093811), (4.17978310585022, -1.5285530090332031),
                                 (3.9356744289398193, -1.4693603217601776), (3.698868989944458, -1.3854924142360687),
                                 (3.473079562187195, -1.2754787802696228), (3.262205958366394, -1.139068365097046),
                                 (3.073397397994995, -0.9735949039459229), (2.915637493133545, -0.7784214168787003),
                                 (2.772194027900696, -0.5720889419317245), (2.6222718954086304, -0.37040794640779495),
                                 (2.467965006828308, -0.17205580323934555), (2.3118494749069214, 0.024879351258277893),
                                 (2.159198522567749, 0.22450001910328865), (2.013025462627411, 0.42890650033950806),
                                 (1.8838815093040466, 0.6443434506654739), (1.7715399861335754, 0.8690277338027954),
                                 (1.7267290353775024, 1.1139249801635742), (1.795179545879364, 1.3539544939994812),
                                 (1.9495075345039368, 1.5504930019378662), (2.1709965467453003, 1.6630489826202393),
                                 (2.4196224212646484, 1.6980105638504028), (2.6707040071487427, 1.7068659663200378),
                                 (2.921698570251465, 1.6952539682388306), (3.1725308895111084, 1.6803690195083618),
                                 (3.423795461654663, 1.6757025122642517), (3.6750710010528564, 1.6716400384902954),
                                 (3.9263564348220825, 1.6682990193367004), (4.1776509284973145, 1.665706992149353),
                                 (4.428947925567627, 1.66337251663208), (4.68024754524231, 1.6613499522209167),
                                 (4.931551456451416, 1.6598895192146301), (5.182857513427734, 1.6590120196342468),
                                 (5.434164524078369, 1.6582504510879517), (5.685471534729004, 1.6577354669570923),
                                 (5.936779975891113, 1.657677948474884), (6.188086986541748, 1.658096969127655),
                                 (6.439394474029541, 1.6585825085639954), (6.69045352935791, 1.6669864654541016),
                                 (6.937283992767334, 1.7131749987602234), (7.173457384109497, 1.7984774708747864),
                                 (7.392812967300415, 1.920696496963501), (7.589590549468994, 2.0766850113868713),
                                 (7.75855827331543, 2.2624370455741882), (7.8950676918029785, 2.473097562789917),
                                 (7.985527753829956, 2.7070255279541016), (8.019554615020752, 2.955344557762146),
                                 (7.978786468505859, 3.2017905712127686), (7.834359407424927, 3.404463529586792),
                                 (7.617611885070801, 3.529360055923462), (7.376079082489014, 3.5976449251174927),
                                 (7.127588987350464, 3.634613513946533), (6.877749443054199, 3.661787509918213)]
