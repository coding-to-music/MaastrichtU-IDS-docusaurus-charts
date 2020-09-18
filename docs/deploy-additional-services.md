---
id: deploy-additional-services
title: Additional services
---

Additional services available with easy installation on the **Data Science Research Infrastructure**.

Feel free to propose new services using [pull requests](https://github.com/MaastrichtU-IDS/dsri-documentation/pulls) or request new ones by creating a [new issues](https://github.com/MaastrichtU-IDS/dsri-documentation/issues).

A service can be easily deployed from a [Docker image](/dsri-documentation/docs/guide-dockerfile-to-openshift).


## Apache Flink

[Apache Flink](https://flink.apache.org/) enables processing of Data Streams using languages such as Java or Scala .

Run Apache Flink in your project using [vemonet/flink-on-openshift](https://github.com/vemonet/flink-on-openshift)

⚠️ At the moment the PVC name needs to be changed before creating the deployment in files `jobmanager-deployment.yaml` and `taskmanager-deployment.yaml`

```shell
git clone https://github.com/vemonet/flink-on-openshift.git
cd flink-on-openshift
# Change the PVC name in YAML files
oc project my-project
./create_deployment.sh
```

Use this command to get the Flink Jobmanager pod id and copy file to the pod.

```shell
oc get pod --selector app=flink --selector component=jobmanager --no-headers -o=custom-columns=NAME:.metadata.name

# Example creating the workspace folder and copying the RMLStreamer.jar to the pod
oc exec <pod_id> -- mkdir -p /mnt/workspace/resources
oc cp workspace/resources/RMLStreamer.jar <pod_id>:/mnt/
```

> [Let us know](https://gitter.im/um-dsri/community) if you are interested in using it, so we could make the deployment easier.

## OpenMPI

OpenMPI can be deployed and run on the DSRI. We use the [MPI Operator from Kubeflow](https://github.com/kubeflow/mpi-operator).

See the [Kubeflow documentation to create a MPI job](https://www.kubeflow.org/docs/components/training/mpi/#creating-an-mpi-job) on OpenShift.

Create Tensorflow Benchmark:

```bash
git clone https://github.com/kubeflow/mpi-operator.git && cd mpi-operator
oc create -f examples/v1alpha2/tensorflow-benchmarks.yaml
```

See the GPU benchmarks for examples of MPI job definitions:

* [MPI TensorFlow benchmark](https://github.com/kubeflow/mpi-operator/blob/master/examples/v1alpha2/tensorflow-benchmarks.yaml)
* [MPI TensorFlow ImageNet benchmark](https://github.com/kubeflow/mpi-operator/blob/master/examples/v1alpha2/tensorflow-benchmarks-imagenet.yaml)

> [Contact us](mailto:dsri-support-l@maastrichtuniversity.nl) to get access to OpenMPI on the DSRI 📬

## File Browser

Deploy a filebrowser on your persistent volume. This will provide a web UI to upload and download data to your DSRI persistent volume.

File browser can be deployed from the [OpenShift Catalog](https://app.dsri.unimaas.nl:8443/console/catalog):

<img src="/dsri-documentation/img/screenshot-deploy-filebrowser.png" alt="Deploy File browser" style="max-width: 100%; max-height: 100%;" />

We can only deploy file browser as a Persistent deployment.

🗄️ **Persistent**: use a Persistent Volume Claim (PVC) for a persistent storage of the data.

The following parameters can be provided:

1. Provide a unique **Application name**. It will be used to generate the application URL.
2. The **Storage name** of the Persistent Volume Claim  (PVC) that will be exposed by the filebrowser.
3. **Storage subpath** in the the Persistent Volume Claim that will be exposed by the filebrowser. Let it empty to use the Root folder of the persistent volume.

You can find the Storage name if you Go to the deployments page > Storage panel.

This deployment require to have  root user enabled on your project. Contact the [DSRI support team](mailto:dsri-support-l@maastrichtuniversity.nl)  or create a [new issues](https://github.com/MaastrichtU-IDS/dsri-documentation/issues) to request root access or to create persistent volume for your project if you don't have them .

Default credentials will be

* login: "admin" 

* password: "admin" 

  *Please change the password in the Filebrowser Web UI once it has been created.*

<img src="/dsri-documentation/img/screenshot-filebrowser-login.png" alt="File browser Web UI" style="max-width: 50%; max-height: 50%;" />