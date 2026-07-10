from fastapi.testclient import TestClient

from .main1 import app
#相对导入只在包中有效，如果单独运行文件，不能用相对导入导入模块
#包：只作为主文件的附属，不单独运行；文件：单独运行


import pytest


# client = TestClient(app)

@pytest.fixture
def client():
    with TestClient(app) as client1:
        yield client1
#pytest是一个测试模块，把测试文件作为包运行


def test_read_main(client):
    response=client.get("/items/foo",headers={"X-Token":"1111"})
    # print(response.status_code)
    assert response.status_code==200
    assert response.json()=={"id": "foo","title": "Foo","description": "这是第一条数据"}
    print("响应信息测试通过")

def test_read_item_bad_token(client):
    response=client.get("/items/foo",headers={"X-Token":"2222"})
    assert response.status_code==400
    assert response.json()=={"detail": "没有权限"}
    print("权限拦截测试通过")

def test_read_item_bad_id(client):
    reponse=client.get("/items/fooo",headers={"X-Token":"1111"})
    assert reponse.status_code==404
    assert reponse.json()=={"detail": "没找到该数据"}
    print("数据不存在报错测试通过")



def test_create_item(client):
    response=client.post(
        "/items/",
        headers={"X-Token":"1111"},
        json={"id": "fooxx","title": "Foo","description":"这是第一条数据"}
    )
    assert response.status_code==200
    assert response.json()=={
        "id": "fooxx",
        "title": "Foo",
        "description": "这是第一条数据"
    }
    print("正常响应测试通过")


def test_create_item_bad_token(client):
    response=client.post(
        "/items/",
        headers={"X-Token":"2222"},
        json={"id": "fooxx", "title": "Foo", "description": "这是第一条数据"}
    )
    assert response.status_code==400
    assert response.json()=={"detail": "没有权限"}
    print("权限拦截测试通过")

def test_create_item_id_exits(client):
    response=client.post(
        "/items/",
        headers={"X-Token":"1111"},
        json={"id": "fooxx", "title": "Foo", "description": "这是第一条数据"}
    )
    assert response.status_code==400
    assert response.json()=={"detail": "id已存在"}
    print("重复数据禁止输入测试通过")


# if __name__=="__main__":
#     test_read_main()
#     test_read_item_bad_token()
#     test_read_item_bad_id()
#     print("-----------------post测试------------------")
#     test_create_item()
#     test_create_item_bad_token()
#     test_create_item_id_exits()