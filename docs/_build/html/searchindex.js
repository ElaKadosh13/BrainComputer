Search.setIndex({docnames:["index","source/braincomputer","source/braincomputer.api","source/braincomputer.cli","source/braincomputer.client","source/braincomputer.db","source/braincomputer.gui","source/braincomputer.gui.static","source/braincomputer.mq","source/braincomputer.parsers","source/braincomputer.proto","source/braincomputer.protocol","source/braincomputer.saver","source/braincomputer.server","source/braincomputer.utils","source/modules"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["index.rst","source/braincomputer.rst","source/braincomputer.api.rst","source/braincomputer.cli.rst","source/braincomputer.client.rst","source/braincomputer.db.rst","source/braincomputer.gui.rst","source/braincomputer.gui.static.rst","source/braincomputer.mq.rst","source/braincomputer.parsers.rst","source/braincomputer.proto.rst","source/braincomputer.protocol.rst","source/braincomputer.saver.rst","source/braincomputer.server.rst","source/braincomputer.utils.rst","source/modules.rst"],objects:{"":{braincomputer:[1,0,0,"-"]},"braincomputer.api":{api:[2,0,0,"-"]},"braincomputer.api.api":{run_api_server:[2,1,1,""],webserver_routers:[2,1,1,""]},"braincomputer.client":{client:[4,0,0,"-"]},"braincomputer.client.client":{upload_sample:[4,1,1,""]},"braincomputer.db":{db:[5,0,0,"-"],mongodb:[5,0,0,"-"]},"braincomputer.db.db":{Db:[5,2,1,""]},"braincomputer.db.db.Db":{close_db:[5,3,1,""],get_all_users:[5,3,1,""],get_color_images_by_user:[5,3,1,""],get_depth_images_by_user:[5,3,1,""],get_feelings_by_user:[5,3,1,""],get_poses_by_user:[5,3,1,""],get_snapshot_by_user_and_ts:[5,3,1,""],get_snapshots_ts_by_user:[5,3,1,""],get_user_by_id:[5,3,1,""],save_to_db:[5,3,1,""]},"braincomputer.db.mongodb":{Mongodb:[5,2,1,""]},"braincomputer.db.mongodb.Mongodb":{close_db:[5,3,1,""],get_all_users:[5,3,1,""],get_color_images_by_user:[5,3,1,""],get_depth_images_by_user:[5,3,1,""],get_feelings_by_user:[5,3,1,""],get_poses_by_user:[5,3,1,""],get_snapshot_by_user_and_ts:[5,3,1,""],get_snapshots_ts_by_user:[5,3,1,""],get_user_by_id:[5,3,1,""],save_to_db:[5,3,1,""]},"braincomputer.gui":{"static":[7,0,0,"-"],html:[6,0,0,"-"],web:[6,0,0,"-"]},"braincomputer.gui.web":{run_server:[6,1,1,""],webserver_routers:[6,1,1,""]},"braincomputer.mq":{mq:[8,0,0,"-"],rabbitmq:[8,0,0,"-"]},"braincomputer.mq.mq":{Mq:[8,2,1,""]},"braincomputer.mq.mq.Mq":{close_queue:[8,3,1,""],consume_from_queue:[8,3,1,""],create_queue:[8,3,1,""],send_to_queue:[8,3,1,""]},"braincomputer.mq.rabbitmq":{Rabbitmq:[8,2,1,""]},"braincomputer.mq.rabbitmq.Rabbitmq":{close_queue:[8,3,1,""],consume_from_queue:[8,3,1,""],create_queue:[8,3,1,""],send_to_queue:[8,3,1,""]},"braincomputer.parsers":{color_image:[9,0,0,"-"],depth_image:[9,0,0,"-"],feelings:[9,0,0,"-"],parsers:[9,0,0,"-"],pose:[9,0,0,"-"]},"braincomputer.parsers.color_image":{parse_color_image:[9,1,1,""]},"braincomputer.parsers.depth_image":{parse_depth_image:[9,1,1,""]},"braincomputer.parsers.feelings":{parse_feelings:[9,1,1,""]},"braincomputer.parsers.parsers":{Parser:[9,2,1,""],Parsers:[9,2,1,""],parse:[9,1,1,""],run_parser:[9,1,1,""],run_parser_mq:[9,1,1,""]},"braincomputer.parsers.parsers.Parser":{callback:[9,3,1,""],create_queue:[9,3,1,""]},"braincomputer.parsers.parsers.Parsers":{get_all_parsers:[9,3,1,""],parse:[9,3,1,""]},"braincomputer.parsers.pose":{parse_pose:[9,1,1,""]},"braincomputer.proto":{messages_pb2:[10,0,0,"-"]},"braincomputer.protocol":{config:[11,0,0,"-"],hello:[11,0,0,"-"],snapshot:[11,0,0,"-"]},"braincomputer.protocol.config":{Config:[11,2,1,""]},"braincomputer.protocol.config.Config":{deserialize:[11,3,1,""],serialize:[11,3,1,""]},"braincomputer.protocol.hello":{Hello:[11,2,1,""]},"braincomputer.protocol.hello.Hello":{deserialize:[11,3,1,""],serialize:[11,3,1,""]},"braincomputer.protocol.snapshot":{SerializedDataStream:[11,2,1,""],Snapshot:[11,2,1,""]},"braincomputer.protocol.snapshot.SerializedDataStream":{deserialize:[11,3,1,""]},"braincomputer.protocol.snapshot.Snapshot":{deserialize:[11,3,1,""],getdt:[11,3,1,""],save_image_data:[11,3,1,""],serialize:[11,3,1,""],to_json:[11,3,1,""]},"braincomputer.saver":{saver:[12,0,0,"-"]},"braincomputer.saver.saver":{Saver:[12,2,1,""],run_saver:[12,1,1,""],save:[12,1,1,""]},"braincomputer.saver.saver.Saver":{callback:[12,3,1,""],handle_queue:[12,3,1,""],save:[12,3,1,""]},"braincomputer.server":{server:[13,0,0,"-"]},"braincomputer.server.server":{Handler:[13,2,1,""],handle_client:[13,1,1,""],run_server:[13,1,1,""]},"braincomputer.server.server.Handler":{run:[13,3,1,""]},"braincomputer.utils":{connection:[14,0,0,"-"],image:[14,0,0,"-"],listener:[14,0,0,"-"],log:[14,0,0,"-"],reader:[14,0,0,"-"],user:[14,0,0,"-"]},"braincomputer.utils.connection":{Connection:[14,2,1,""]},"braincomputer.utils.connection.Connection":{connect:[14,3,1,""],receive:[14,3,1,""],receive_message:[14,3,1,""],send:[14,3,1,""],send_message:[14,3,1,""]},"braincomputer.utils.image":{ColorImage:[14,2,1,""],DepthImage:[14,2,1,""],Image:[14,2,1,""]},"braincomputer.utils.image.Image":{is_empty:[14,3,1,""]},"braincomputer.utils.listener":{Listener:[14,2,1,""]},"braincomputer.utils.listener.Listener":{accept:[14,3,1,""]},"braincomputer.utils.log":{Log:[14,2,1,""]},"braincomputer.utils.reader":{Reader:[14,2,1,""],start_reader:[14,1,1,""]},"braincomputer.utils.reader.Reader":{get_snapshot_data:[14,3,1,""],get_user_data:[14,3,1,""],iterate_snapshots:[14,3,1,""]},"braincomputer.utils.user":{User:[14,2,1,""]},braincomputer:{api:[2,0,0,"-"],cli:[3,0,0,"-"],client:[4,0,0,"-"],db:[5,0,0,"-"],gui:[6,0,0,"-"],mq:[8,0,0,"-"],parsers:[9,0,0,"-"],proto:[10,0,0,"-"],protocol:[11,0,0,"-"],saver:[12,0,0,"-"],server:[13,0,0,"-"],utils:[14,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","method","Python method"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:method"},terms:{"class":[5,8,9,11,12,13,14],"default":8,"function":[5,8,9],"new":[5,8],"static":[1,6],"true":14,The:[4,5,13],accept:14,activ:13,address:8,all:[4,5,8,9],also:[5,8],ani:13,anyth:8,api:[1,15],arg:[5,8,13],argument:[5,8,13],backlog:14,base:[5,8,9,11,12,13,14],befor:8,bind:12,bodi:[8,9,12],by_format:11,callabl:13,callback:[8,9,12],can:8,chang:[5,8],classmethod:[11,14],cli:[1,15],client:[1,15],close:8,close_db:5,close_queu:8,collect:9,color_imag:[1,11,15],colorimag:14,config:[1,15],connect:[1,8,13,15],constructor:13,consum:[8,9,12],consume_from_queu:8,content:15,correct:9,creat:[8,9,12],create_queu:[8,9],data:[5,9,11,12,13,14],data_dir:13,database_url:[2,6],datetim:11,db_url:[5,12],depth_imag:[1,11,15],depthimag:14,deseri:11,differ:[5,8],directori:9,done:8,each:12,easi:[5,8],empti:8,fanout:8,feel:[1,15],field:11,file_path:14,file_stream:14,forev:13,from:[8,9,12,13],get:8,get_:5,get_all_pars:9,get_all_us:5,get_color_images_by_us:5,get_depth_images_by_us:5,get_feelings_by_us:5,get_poses_by_us:5,get_snapshot_by_user_and_t:5,get_snapshot_data:14,get_snapshots_ts_by_us:5,get_user_by_id:5,get_user_data:14,getdt:11,gui:[1,15],handle_cli:13,handle_queu:12,handler:13,has:[5,8],height:14,hello:[1,15],host:[2,4,6,8,13,14],html:[1,15],imag:[1,15],image_data:14,implement:[5,8],index:0,initi:[5,8],insert:5,invok:13,is_empti:14,iterate_snapshot:14,just:[5,8],kei:[8,12],keyword:13,kwarg:13,line:[5,8],listen:[1,15],log:[1,15],mai:[4,13],make:[5,8],messag:14,messages_pb2:[1,15],method:[5,8,9,12,13],modul:[0,15],mongodb:[1,15],mq_url:[9,12],name:8,need:[5,8],none:[11,14],number_of_field:11,object:[5,8,9,11,12,13,14],one:12,overrid:13,packag:15,page:0,paramet:8,pars:9,parse_color_imag:9,parse_depth_imag:9,parse_feel:9,parse_pos:9,parser:[1,8,12,15],parser_typ:[9,12],parsing_funct:9,pass:13,path:[4,11,12],port:[2,4,6,8,13,14],pose:[1,15],produc:9,properti:[9,12],proto:[1,15],protocol:[1,15],publish:[8,9,13],queri:5,queue:[8,9,12],rabbitmq:[1,15],raw_data_path:9,reader:[1,15],receiv:14,receive_messag:14,reciev:8,replac:[5,8],repres:13,respect:13,reuseaddr:14,root:11,rotat:11,rout:8,run:13,run_api_serv:2,run_pars:9,run_parser_mq:9,run_sav:12,run_serv:[6,13],save:12,save_image_data:11,save_to_db:5,saver:[1,15],search:0,send:[4,8,14],send_messag:14,send_to_queu:8,sequenti:13,serial:11,serialized_data:11,serialized_data_stream:11,serializeddatastream:11,server:[1,4,8,9,15],set:8,size:14,snapshot:[1,4,5,9,15],sock:14,some:4,sourc:[2,4,5,6,8,9,11,12,13,14],standard:13,start_read:14,subclass:13,submodul:[1,15],subpackag:15,sure:[5,8],tabl:5,take:4,taken:13,target:13,thi:[9,13],those:[5,8],thread:13,time:4,timestamp:5,to_json:11,topic:[8,9],translat:11,type:8,updat:5,upload_sampl:4,use:[5,8],user:[1,5,11,15],user_birthdai:[11,14],user_feel:11,user_gend:[11,14],user_id:[5,11,14],user_nam:[11,14],util:[1,15],want:[5,8],web:[1,15],webserver_rout:[2,6],width:14,you:[5,8,13]},titles:["Welcome to BrainComputer\u2019s documentation!","braincomputer package","braincomputer.api package","braincomputer.cli package","braincomputer.client package","braincomputer.db package","braincomputer.gui package","braincomputer.gui.static package","braincomputer.mq package","braincomputer.parsers package","braincomputer.proto package","braincomputer.protocol package","braincomputer.saver package","braincomputer.server package","braincomputer.utils package","braincomputer"],titleterms:{"static":7,api:2,braincomput:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],cli:3,client:4,color_imag:9,config:11,connect:14,content:[1,2,3,4,5,6,7,8,9,10,11,12,13,14],depth_imag:9,document:0,feel:9,gui:[6,7],hello:11,html:6,imag:14,indic:0,listen:14,log:14,messages_pb2:10,modul:[1,2,3,4,5,6,7,8,9,10,11,12,13,14],mongodb:5,packag:[1,2,3,4,5,6,7,8,9,10,11,12,13,14],parser:9,pose:9,proto:10,protocol:11,rabbitmq:8,reader:14,saver:12,server:13,snapshot:11,submodul:[2,4,5,6,8,9,10,11,12,13,14],subpackag:[1,6],tabl:0,user:14,util:14,web:6,welcom:0}})