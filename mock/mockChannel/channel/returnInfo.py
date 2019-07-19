# --**coding:utf-8**--


def nanjingZs():
    resturnMessage = {
        "MESSAGE": "身份证号与姓名匹配，且比对成功",
        "guid": "20180417170941_V8dr34p9_1000007",
        "detail": {
            "resultCode": "1001",
            "resultInfo": {
                "score": "10"
            },
            "resultMsg": "系统判断为同一人"
        },
        "RESULT": "1"
    }
    return resturnMessage


def OCRBankCard():
    bankCardInfo = {
        "result": {
            "image_id": "wZVniECOHw2cR7wxTa19jA==",
            "request_id": "1558455616,312dd4b6-1266-4b18-9e8a-28b24af8126b",
            "time_used": 376,
            "bank_cards": [{
                "organization": ["union"],
                "number": "6228480369467244975",
                "bank": "u519cu4e1au94f6u884c",
                "bound": {
                    "left_bottom": {
                        "y": 652,
                        "x": 84
                    },
                    "right_top": {
                        "y": 101,
                        "x": 873
                    },
                    "right_bottom": {
                        "y": 591,
                        "x": 909
                    },
                    "left_top": {
                        "y": 162,
                        "x": 48
                    }
                }
            }]
        },
        "statusCode": 200,
        "success": True
    }
    return bankCardInfo


jiupaiFourElements = "rspCode=IPS00000&requestId=754d01562d1d420c84b5d5a32729a293&signType=RSA&resultStatus=S&charset=02&serverSign=7A640595DD38290EAD0097AE972D64AF0746E025BE4F2E1C806926FB51BA95D487CCDF3DAC9EB04EC0208B2BB0DD36B8A66CCC53DEB74558CC5236E6ABCA4A4F34159841297FF147B6AAA61A67BE9C239DE282334ACE8A5747889DD472163E4FD7E934A477148BE60A5726D98FFA4FD38EF1892DBD8DB1A8E9507E663B834AE8&rspMessage=请求成功&version=1.0&responseId=o1dbdluitc2x0gB9Hv4WO8Na-8kgYzPC&serverCert=3082039B30820283A0030201020214382A3E05EE498420ECAD3939A63C4040039BBCE7300D06092A864886F70D0101050500307F310B300906035504061302434E31273025060355040A0C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB8311E301C060355040B0C15E68A80E69CAFE983A8EFBC88E4BC81E4B89AEFBC893127302506035504030C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB8301E170D3138303631393037353933375A170D3231303631383037353933375A30818D3128302606092A864886F70D0109011619383130303638323638393934406B696E67706173732E636F6D3118301606035504030C0F383030303733313030303530303036311E301C060355040B0C15E68A80E69CAFE983A8EFBC88E4BC81E4B89AEFBC8931273025060355040A0C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB830819F300D06092A864886F70D010101050003818D0030818902818100D60752985B589E02545E9D0357CC7BC506AA149D12F8F5883173A571C1780685CAE4C9E4DE4318267EDCEED49D33127C1906AD9621648552DDF54CBF92CD93892B467E37ABC1AFEEC9EE4FAE813EC37F0765F709C3182BAA591087AF2F09DE22A1AF485B141B663DC4C68D7F04DD02E27FC572B36E51C7A4601542520A2508890203010001A3818330818030090603551D1304023000300B0603551D0F0404030205A030660603551D1F045F305D305BA059A0578655687474703A2F2F746F7063612E69747275732E636F6D2E636E2F7075626C69632F697472757363726C3F43413D35454245394444443041394636423243313638374444463444373330334445303630334234443730300D06092A864886F70D01010505000382010100904FEC0717A595FD2198D58111C818F071E8B5861CD0D980616740370ADB8982BD51544871014ED8584E6DC7F839D911AFD31404B92D4850431E7A3EFD68EADD9EC69FD28CF9B2030FAF02045621993DAB5C8BF218F120AF8C5D6D68DD2A2C5E23BA524FA05B9EA9A4699250BB988C92D1A1D650212D0522B9966ED93E7118DDF721887D6C5E467725BCF4CE971FCDD46117E376A97880DA5DC5E475FB52D4D72AC45CF87FD6ABF29F691822661C490009A3B5A6A0B440E91FC62604EF0A7BE38B4D8DE68CC81AFE887796485055581A594F51773C284242E92B1404F4FA5EECDFD6FCA5B645577547FEE8C10614F6C7F023E54C938444A3119CB9BC7CDBF65E&merchantId=&responseTime=20190522011016"
jiupaiTwoElements = "ischarge=0&rspCode=IPS00000&requestId=202b7fd4728c4006a6b7ad4f56bfb919&status=&signType=RSA&charset=02&serverSign=09FC4A29882FA9F4FDE042A32C068A6F16DAB97FEF1BB53899D8BCE968F5F2EB9BA99C0D8398015F2F8C055CD77CB552F93CC3381B9C61255F49881A6B28CD5001E14977147C0356CBC6A9DD44E2B07E751AF9B855AAE6F14AA6AEF9F82E3D5A485E75B91FEDE183CDFC5738D22FD8E21AC41C25F56DBE58316B24881C4BCFC9&rspMessage=认证通过&version=1.0&responseId=386780bddee945199519ee37c686cb63&hashIdNo=&serverCert=3082039B30820283A0030201020214382A3E05EE498420ECAD3939A63C4040039BBCE7300D06092A864886F70D0101050500307F310B300906035504061302434E31273025060355040A0C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB8311E301C060355040B0C15E68A80E69CAFE983A8EFBC88E4BC81E4B89AEFBC893127302506035504030C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB8301E170D3138303631393037353933375A170D3231303631383037353933375A30818D3128302606092A864886F70D0109011619383130303638323638393934406B696E67706173732E636F6D3118301606035504030C0F383030303733313030303530303036311E301C060355040B0C15E68A80E69CAFE983A8EFBC88E4BC81E4B89AEFBC8931273025060355040A0C1EE4B99DE6B4BEE5A4A9E4B88BE694AFE4BB98E69C89E99990E585ACE58FB830819F300D06092A864886F70D010101050003818D0030818902818100D60752985B589E02545E9D0357CC7BC506AA149D12F8F5883173A571C1780685CAE4C9E4DE4318267EDCEED49D33127C1906AD9621648552DDF54CBF92CD93892B467E37ABC1AFEEC9EE4FAE813EC37F0765F709C3182BAA591087AF2F09DE22A1AF485B141B663DC4C68D7F04DD02E27FC572B36E51C7A4601542520A2508890203010001A3818330818030090603551D1304023000300B0603551D0F0404030205A030660603551D1F045F305D305BA059A0578655687474703A2F2F746F7063612E69747275732E636F6D2E636E2F7075626C69632F697472757363726C3F43413D35454245394444443041394636423243313638374444463444373330334445303630334234443730300D06092A864886F70D01010505000382010100904FEC0717A595FD2198D58111C818F071E8B5861CD0D980616740370ADB8982BD51544871014ED8584E6DC7F839D911AFD31404B92D4850431E7A3EFD68EADD9EC69FD28CF9B2030FAF02045621993DAB5C8BF218F120AF8C5D6D68DD2A2C5E23BA524FA05B9EA9A4699250BB988C92D1A1D650212D0522B9966ED93E7118DDF721887D6C5E467725BCF4CE971FCDD46117E376A97880DA5DC5E475FB52D4D72AC45CF87FD6ABF29F691822661C490009A3B5A6A0B440E91FC62604EF0A7BE38B4D8DE68CC81AFE887796485055581A594F51773C284242E92B1404F4FA5EECDFD6FCA5B645577547FEE8C10614F6C7F023E54C938444A3119CB9BC7CDBF65E&name=&merchantId=800000100020143&responseTime=20190522000005"