#  2️⃣ | Provision Infra

??? note "Step 6: Provision infra with `azd` in tab 2️⃣"

    1. Stay in tab 2️⃣ - enter `azd up` and follow prompts
        1. Enter a new environment name - use `AITOUR`
        1. Select a subscription - pick the same one from step 5.
        1. Select a location - pick `francecentral` (or `swedencentral`)
        1. You should see: _"You can view detailed progress in the Azure Portal ..."_
    1. Provisioning takes a while to complete - let's track status next.
    1. ✅ | Your Azure infra is currently being provisioned..

??? note "Step 7: Track provisioning status in tab 3️⃣"

    1. Switch to the Azure Portal in tab 3️⃣
    1. Click on Resource Groups - see: `rg-AITOUR`
    1. Click on `rg-AITOUR` - see `Deployments` under **Essentials**
    1. Click `Deployments` - see Deployments page with activity and status ...
    1. Wait till all deployments complete - **this can take 20-25 minutes**
    1. See `Overview` page - **you should have 35 Deployment Items**
    1. See `Overview` page - **you should have 15 Deployed Resources**
    1. Return to tab 2️⃣ and look at terminal - you should see:
        1. **SUCCESS: Your up workflow to provision and deploy to Azure completed in XX minutes YY seconds.**
    1. ✅ | Your Azure infra is ready!

The last step provisions the Azure infrastructure **and** deploys the first version of your application. We are now ready to get to work.

---

!!! info "Next → 3️⃣ [Let's Explore App Infrastructure](./../03-Workshop-Build/03-infra.md) before we start building!"
