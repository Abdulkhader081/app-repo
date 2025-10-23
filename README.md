# app-repo
Application Source Code Repository: Contains application code.
I have created CI pipeline that deploys a Phython web application to a Kubernetes cluster using a GitOps workflow with ArgoCD 
  app-repo/ which 
	 Contains the application source code and the CI pipeline. 
	 CI pipeline includes stages like unit tests , Builds/packages the application into docker image and publishes container images to Docker Registry.
	 And final stage includes Updating the deployment manifest (or Helm values.yaml) in gitops-repo with the new image tag.
