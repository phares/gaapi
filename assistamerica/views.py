from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
import cx_Oracle
from assistamerica.serializers import PolicySerializer
from decouple import config


class Policy(viewsets.ViewSet):
    serializer_class = PolicySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        res = None
        return Response(res)

    def policy(self, request, *args, **kwargs):

        result_list = []
        policy_dict = {}
        count = 0

        try:
            policy_no = request.data.get('policy_no')
            db_credentials = config('DB_CREDENTIALS')
            con = cx_Oracle.connect(db_credentials)
            cur = con.cursor()
            params = {'policy_no': policy_no, 'limit': 1}
            cur.execute('select * from  where pol_no = :policy_no and ROWNUM <= :limit', params)

            for p in cur:
                count += 1
                policy_dict["policy_no"] = p[0]
                policy_dict["online_ref_no"] = p[1]
                policy_dict["cust_code"] = p[2]
                policy_dict["cust_name"] = p[3]
                policy_dict["assr_code"] = p[4]
                policy_dict["assr_name"] = p[5]
                policy_dict["email_id"] = p[6]
                policy_dict["telephone_no"] = p[7]
                policy_dict["from_date"] = p[8]
                policy_dict["to_date"] = p[9]
                policy_dict["result"] = True

            if count == 0:

                policy_dict["policy_no"] = policy_no
                policy_dict["detail"] = "No record matching policy no. found"
                policy_dict["result"] = False

        except Exception as e:
            policy_dict["detail"] = str(e)  # 'Unable to fetch result'
            policy_dict["result"] = False

        result_list.append(policy_dict)
        policy = PolicySerializer(result_list, many=True).data
        return Response(policy)




