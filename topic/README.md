## Vue Network Graph using Python NetworkX

### Reference
 - [V-Network-Graph](https://dash14.github.io/v-network-graph/reference.html#configurations)
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 - [Axios](https://www.npmjs.com/package/axios)

### Setup
BACKEND (NetworkX)
```
$ cd api
$ pip install -r requirement.txt
$ python app.py
```

Frontend (v-network-graph)
```
$ cd webapp
$ npm install
$ npm run serve
```

### Load Graph from JSON
Code-ref: `Network.vue`

### Load Graph using Axios
Code-ref: `Async.vue`, `components/AsyncNetworkGraph`

### Deployment reference
Backend: [deployment branch](https://github.com/EngSiangTeo/IS434/tree/deployment)
Frontend: [frontend-deployment branch](https://github.com/EngSiangTeo/IS434/tree/frontend-deployment)

### Preview
![image](https://user-images.githubusercontent.com/56392203/155067409-6117b12a-6189-4cc1-873c-1ac9eb99bf49.png)
![image](https://user-images.githubusercontent.com/56392203/155067487-55a5d112-f96a-4942-b448-e21b6458b61a.png)
