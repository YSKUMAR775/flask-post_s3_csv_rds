import pymysql


def insert_rds(new_list):

    mydb = pymysql.connect(host='database.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                           user='root',
                           password='yskumar775',
                           db='aws3'
                           )
    cur = mydb.cursor()

    # for i in new_list:
    #     a = i['id']
    #     b = i['period']
    #     c = i['short_descriptions']
    #     d = i['temperatures']
    #
    #     query_1 = "insert into aws3_table values('" + str(a) + "','" + str(b) + "','" + str(c) + "','" + str(d) + "')"
    #     cur.execute(query_1)
    #
    # mydb.commit()
    # return jsonify({'url': file_path})

    query_2 = "select * from aws3_table"
    cur.execute(query_2)
    s = cur.fetchall()

    total_list = []
    for i in s:
        all_dict = {'id': i[0], 'period': i[1], 'short_descriptions': i[2], 'temperatures': i[3]}
        total_list.append(all_dict)

    # print(total_list)

    return total_list
