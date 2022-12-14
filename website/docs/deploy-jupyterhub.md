---
id: deploy-jupyterhub
title: JupyterHub
---

JupyterHub is ideal to enable multiple users easily start predefined workspaces in the same project. 


## 🧊 Install kfctl

You will need to have the usual `oc` tool installed, and to install `kfctl` on your machine, a tool to deploy Kubeflow applications, download the [latest version for your OS 📥️](https://github.com/kubeflow/kfctl/releases) 

You can then install it by downloading the binary and putting it in your path, for example on Linux:

```bash
wget https://github.com/kubeflow/kfctl/releases/download/v1.2.0/kfctl_v1.2.0-0-gbc038f9_linux.tar.gz
tar -xzf kfctl_v1.2.0-0-gbc038f9_linux.tar.gz
sudo mv kfctl /usr/local/bin/
```

Clone the repository with the DSRI custom images and deployments for the OpenDataHub platform, and go to the `kfdef` folder:

```bash
git clone https://github.com/MaastrichtU-IDS/odh-manifests
cd odh-manifests/kfdef
```

## 🪐 Deploy JupyterHub and Spark

:::info Go the the kfdef folder

All scripts need to be run from the `kfdef` folder 📂

:::

You can deploy JupyterHub with 2 different authentications system, use the file corresponding to your choice:

* For the default DSRI authentication use `kfctl_openshift_dsri.yaml`

* For GitHub authentication use `kfctl_openshift_github.yaml`

  * You need to create a new GitHub OAuth app: https://github.com/settings/developers

  * And provide the GitHub client ID and secret through environment variable before running the start script:

    ```bash
    export GITHUB_CLIENT_ID=YOUR_CLIENT_ID
    export GITHUB_CLIENT_SECRET=YOUR_CLIENT_SECRET
    ```

First you will need to change the `namespace:` in the file you want to deploy, to provide the project where you want to start JupyterHub (currently `opendatahub-ids`), then you can deploy JupyterHub and Spark with `kfctl`:

```bash
./start_odh.sh kfctl_openshift_dsri.yaml
```

🗄️ Persistent volumes are automatically created for each instance started in JupyterHub to insure persistence of the data even JupyterHub is stopped. You can find the persistent volumes in the DSRI web UI, go to the **Administrator** view > **Storage** > **Persistent Volume Claims**.


<!--

:::warning Restricted user

The users will be able to install new `pip` packages in their JupyterLab instance, but they will not have `sudo` privileges (so they cannot install `apt` or `yum` packages for example). This can be changed by editing the KubeSpawner python script in the ConfigMap to use `serviceAccountName: anyuid`

::: -->