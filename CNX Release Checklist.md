The following should be checked every release cycle before handing off to DevOps for a staging deploy. Use the [CNX Repos Dashboard](https://ks52.web.rice.edu/cnx-repos.html) to help. You can uncheck everything below to start over for the next release.

Be sure to verify version numbers _after_ every deployment using the top-level `history.txt` file before starting/resuming testing.

### But first: little things that are easily missed and delay testing
- oer.exports `version.txt`
- RhaptosPrint version regressions: DevOps needs to keep `cnx-deploy/environments/__prod_envs/files/versions.cfg` updated for every cnx-deploy tag and deployment
- Revs that don't get into cnx-deploy 

**Note:** You can copy and paste the following checklists into a new issue and make them collapsible/expandable by wrapping markdown with the following tags in Github:
```
<details>
<summary>Click here to see full checklist</summary>
[CHECKLIST MARKDOWN HERE]
</details>
```
See an example here: https://github.com/Connexions/webview/issues/1830

## Books repos

- [ ] **oer.exports** (*Helene*)
	- [ ] https://github.com/Connexions/oer.exports/blob/master/version.txt should match current release
	- [ ] Release created in https://github.com/Connexions/oer.exports/releases
	- [ ] New RhaptosPrint egg should be built by DevOps (they need the version number)
- [ ] **cnx-recipes** (*Helene*)
	- [ ] Release created in https://github.com/Connexions/cnx-recipes/releases
	- [ ] PyPi version revved
	- [ ] cnx-deploy: `environments/__prod_envs/files/publishing-requirements.txt` should be updated -- a bot will automatically create this PR, which will need to be reviewed and merged.
- [ ] **webview** (*Helene*)
 	- [ ] Release created in https://github.com/Connexions/webview/releases
	- [ ] Tarball for version needs to be available at https://packages.cnx.org/js-builds/ (I think Jenkins builds this automatically?)
	- [ ] cnx-deploy: needs a manual PR opened, reviewed, and merged to update `environments/__prod_envs/vars/versions.yml`

## CNX repos
Any combination of the below repos can be updated for any given release. We need to make sure the ones that do get released are **updated in PyPi** where applicable, as well as in **cnx-deploy**. 

Again: **not every repo below will be updated for every release.** You can check off the repos that will not be included if it makes tracking easier.

And, also, **there are other CNX repos that are not listed below**. 

- [ ] **cnx-archive** (*Ross*)
 	- [ ] Release tag created in GitHub
 	- [ ] PyPi version revved
	- [ ] cnx-deploy: 2 files need updating (a bot will automatically create this PR, which will need to be reviewed and merged):
		- ` environments/__prod_envs/files/archive-requirements.txt`
		- `environments/__prod_envs/files/publishing-requirements.txt` 
- [ ] **cnx-db** (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
	- [ ] cnx-deploy: 3 files need updating (a bot will automatically create this PR, which will need to be reviewed and merged.):
		- ` environments/__prod_envs/files/archive-requirements.txt`
		- `environments/__prod_envs/files/press-requirements.txt` 
		-  `environments/__prod_envs/files/publishing-requirements.txt`
- [ ] **cnx-easybake** (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
	- [ ] cnx-deploy: `environments/__prod_envs/files/publishing-requirements.txt` should be updated -- a bot will automatically create this PR, which will need to be reviewed and merged.
- [ ] **cnx-epub** (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
	- [ ] cnx-deploy: `environments/__prod_envs/files/publishing-requirements.txt` should be updated -- a bot will automatically create this PR, which will need to be reviewed and merged. 
- [ ] **cnx-press** (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] cnx-deploy: `environments/__prod_envs/vars/versions.yml` should be updated -- a bot will automatically create this PR, which will need to be reviewed and merged.
- [ ] **cnx-publishing** (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
	- [ ] cnx-deploy: `environments/__prod_envs/files/publishing-requirements.txt` should be updated -- a bot will automatically create this PR, which will need to be reviewed and merged.
- [ ] **nebuchadnezzar** (batch publishing client) (*Dante*) - *no cnx-deploy change required*
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
- [ ] **Other CNX repos** such as `cnxml`, `rhaptos.cnxmlutils`, etc. (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] PyPi version revved
	- [ ] cnx-deploy should be updated -- PRs may or may not be automatically generated.
- [ ] **Random legacy/zope repos** such as `Products.CNXMLDocument`,  `Products.RhaptosModuleEditor`, etc. -- anything that starts with `Products.*` (*Ross*)
 	- [ ] Release tag created in GitHub
	- [ ] dist.rhaptos.org updated
	- [ ] cnx-deploy: `environments/__prod_envs/files/versions.cfg` should be updated via manual PRs 

## Other links
- [TestRail Milestones for CNX](https://openstax.testrail.com/index.php?/milestones/overview/7)
- [Trello for DevOps: Staging card template](https://trello.com/c/TjO1ud99/218-cnxbooks-deploy-to-staging-servers-for-2018xxxx-release)
  - [Staging card example (8/13/18 release)](https://trello.com/c/3GhSiceI/226-cnxbooks-deploy-to-staging-servers-for-20180813-release)
- [Trello for DevOps: Prod card template](https://trello.com/c/ScGRxZAO/213-cnxbooks-deploy-to-production-servers-for-2018xxxx-release)
  - [Prod card example (8/13/18 release)](https://trello.com/c/bQ4rBy4j/228-cnxbooks-deploy-to-production-servers-for-20180813-release)
- [Further reading about this process (outdated)](https://docs.google.com/document/d/1e3YnfOq1o9otTObKntELk6oxd9zzXDMhoJydw2QnAWw/edit#heading=h.41lwwxygk8be)

