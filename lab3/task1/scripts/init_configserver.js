rs.initiate({_id: "rs_config_server", configsvr: true, version: 1, members: [ { _id: 0, host : 'config_server_1:27017' }, { _id: 1, host : 'config_server_2:27017' }, { _id: 2, host : 'config_server_3:27017' } ] })