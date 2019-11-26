---
id: openshift-deploy-jupyter
title: Deploy Jupyter Notebooks
---

[![Jupyterlab](/dsri-documentation/img/jupyter_logo.png)](https://jupyter.org/)

Feel free to propose new services using [pull requests](https://github.com/MaastrichtU-IDS/dsri-documentation/pulls) or request new ones by creating a [new issues](https://github.com/MaastrichtU-IDS/dsri-documentation/issues).

---

## Recommended deployment

Select `Jupyter Notebook Quickstart` from the [DSRI services catalog](https://app.dsri.unimaas.nl:8443/console/catalog) web UI while on the right project.

* *Application_name*: the unique name of your application
  * e.g. `nb-tensorflow-word2vec`
* *Notebook_interface*
  * `classic`: Jupyter notebook web UI.
  * `lab`: Jupyterlab web UI.
* *Builder_image*
  * `s2i-minimal-notebook:3.6` : minimal jupyter notebook
  * `s2i-scipy-notebook:3.6` : notebook with popular scientific libraries pre-installed
  * `s2i-tensorflow-notebook:3.6` : notebook with tensorflow libraries for machine learning.
* *Git_repository_url*: the notebook git repository. Place a `requirements.txt` file at the root to install additional libraries.
  * See [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) as example.
* *Context_dir*: should enable to select working directory. But at the moment fails if directory doesn't exist.
  * By default the working directory is `/opt/app-root/src` (TODO: try `/srv`)
  * See [jupyter-on-openshift JupyterHub readme](https://github.com/jupyter-on-openshift/jupyterhub-quickstart#allocating-persistent-storage-to-users) and [OpenShift official documentation](https://blog.openshift.com/jupyter-on-openshift-part-4-adding-a-persistent-workspace/) to enable using persistent volumes.

> Built from [jupyter-on-openshift](https://github.com/jupyter-on-openshift/jupyter-notebooks).

## Jupyter as root user

This method require to have enabled root user on your project. Contact the [DSRI support team](mailto:dsri-support-l@maastrichtuniversity.nl) to request root access.

Use [amalic/jupyterlab](https://hub.docker.com/r/amalic/jupyterlab/) Docker image.

* Image name:
  
  ```
  amalic/jupyterlab
  ```
  
* Environment variables:
  
  * `PASSWORD=my_password`
  
* Mounted volume: `/notebooks`

> Network port: `8888`

> Use [OpenShift secrets](/dsri-documentation/docs/openshift-secret) to provide password in a secure manner. (**TODO:** improve doc).

## Anaconda and Tensorflow with Jupyter

Another option to run Jupyter notebooks with Anaconda and Tensorflow installed.

Use [jupyter/tensorflow-notebook](https://hub.docker.com/r/jupyter/tensorflow-notebook) official Docker image.

* Image name:

  ```shell
  jupyter/tensorflow-notebook
  ```
  
* Environment variables:

  * `JUPYTER_ENABLE_LAB=yes` (optional)

* Mounted path: `/home/jovyan`

> Go to the `pod logs` to get the `login token`.

