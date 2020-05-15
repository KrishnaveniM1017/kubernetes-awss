metadata:
  creationTimestamp: "2020-05-15T10:45:57Z"
  name: zip.k8s.valaxy.in
spec:
  api:
    dns: {}
  authorization:
    rbac: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in
  configStore: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in
  dnsZone: valaxy.in
  docker:
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay2,overlay,aufs
    version: 18.09.9
  etcdClusters:
  - backups:
      backupStore: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in/backups/etcd/main
    cpuRequest: 200m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-ca-central-1b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: main
    provider: Manager
    version: 3.3.10
  - backups:
      backupStore: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in/backups/etcd/events
    cpuRequest: 100m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-ca-central-1b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: events
    provider: Manager
    version: 3.3.10
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.16.9
    insecureBindAddress: 127.0.0.1
    insecurePort: 8080
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: zip.k8s.valaxy.in
    configureCloudRoutes: true
    image: k8s.gcr.io/kube-controller-manager:v1.16.9
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.16.9
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.16.9
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.16.9
  masterInternalName: api.internal.zip.k8s.valaxy.in
  masterKubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.zip.k8s.valaxy.in
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://zip.k8s.valaxy.in/zip.k8s.valaxy.in/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: ca-central-1b
    type: Public
    zone: ca-central-1b
  topology:
    dns:
      type: Private
    masters: public
    nodes: public
