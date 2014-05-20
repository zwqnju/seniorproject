import networkx as nx
import json
import math

from operator import itemgetter

### Function: calculate centrality
### Details: 
def calculate_centrality(G):
	# dc_dumps = json.dumps(nx.degree_centrality(G).items(),sort_keys=True,indent=4)
	# dc_loads = json.loads(dc_dumps)
	dc_sorted = sorted(nx.degree_centrality(G).items(), key=itemgetter(0), reverse=True)
	bc_sorted = sorted(nx.betweenness_centrality(G).items(), key=itemgetter(0), reverse=True)
	clc_sorted = sorted(nx.closeness_centrality(G).items(), key=itemgetter(0), reverse=True)
	coc_sorted = sorted(nx.communicability_centrality(G).items(), key=itemgetter(0), reverse=True)
	lc_sorted = sorted(nx.load_centrality(G).items(), key=itemgetter(0), reverse=True)
	cfbc_sorted = sorted(nx.current_flow_betweenness_centrality(G).items(), key=itemgetter(0), reverse=True)
	# print ec_sorted[0]
	
	developer_centrality = []

	for i in range (0, len(dc_sorted)):
		# if ( not dc_sorted[i][0] == bc_sorted[i][0] == clc_sorted[i][0] == coc_sorted[i][0] == lc_sorted[i][0] == cfbc_sorted[i][0]):
		# 	print 'false'
		developer_centrality.append({
			'name': dc_sorted[i][0],
		 	'degree': dc_sorted[i][1],
			'betweenness': bc_sorted[i][1],
			'closeness': clc_sorted[i][1],
			'communicability': coc_sorted[i][1],
			'load': lc_sorted[i][1],
			'current_flow_betweenness': cfbc_sorted[i][1]
		 })

	return developer_centrality
### Function:end

### Function: write to file
def writefile(developer_centrality, relation, version):
	c_file = open("public/wordpress/centrality_developer_"+relation+"_"+version+".json","w")
	#c_file = open('app/subservice/test.json','w')
	c_file.write(json.dumps(calculate_centrality(G),sort_keys=True,indent=4))
# Function: end


version = [ '15', '20', '21', '22', '23', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
relation = [ 'comment', 'commit', 'work']


### Function: read source file
for i in range(0, len(version)):
	for j in range(0, len(relation)):
		d_file = file("public/wordpress/network_developer_"+relation[j]+"_"+version[i]+".json")
		d = json.load(d_file)

		G=nx.Graph()
		# e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2)]
		# G.add_weighted_edges_from(e)
		# G.add_node("spam")
		# G.add_edge(1,2)
		# print(G.nodes())
		# print(G.edges())

		e = []
		[ e.append( (edge['developer1'], edge['developer2'], edge['count']) )
			for edge in d ]
		G.add_weighted_edges_from(e)

		writefile(calculate_centrality(G), relation[j], version[i])
### Function:end







