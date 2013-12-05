# Copyright (c) 2010-2013 Novell, Inc.
# Licensed under the terms of the MIT license.

Feature: Test Powermanagement

  Scenario: Is the powermanagement page accessible
    Given I am on the Systems overview page of this client
      And I follow "Provisioning" in the content area
      And I follow "Power Management" in the content area
     Then I should see a "Power Management Settings" text
      And I should see a "IPMI" text
      And I should see a "Save" button

  Scenario: Save powermanagement values
    Given I am on the Systems overview page of this client
      And I follow "Provisioning" in the content area
      And I follow "Power Management" in the content area
     When I enter "192.168.254.254" as "powerAddress"
      And I enter "admin" as "powerUsername"
      And I enter "qwertz" as "powerPassword"
      And I click on "Save"
     Then I should see a "Power settings saved" text
      And the cobbler report contains "Power Management Address       : 192.168.254.254"
      And the cobbler report contains "Power Management Password      : qwertz"
      And the cobbler report contains "Power Management Type          : ipmitool"
      And the cobbler report contains "Power Management Username      : admin"

    Scenario: check powermanagement in SSM
        Given I am on the Systems page
         When I check this client
          And I follow "System Set Manager" in the left menu
         Then I should see a "Configure power management" link in the content area
          And I should see a "power management operations" link in the content area

    Scenario: check powermanagement SSM configuration
        Given I am on the Systems page
         When I follow "System Set Manager" in the left menu
          And I follow "Configure power management" in the content area
         Then I should see this client as link
          And I should see a "Change Power Management Configuration" text
          And I should see a "Type" text
          And I should see a "Network address" text
          And I should see a "Username" text
          And I should see a "Password" text
          And I should see a "System identifier" text
          And I should see a "Update" button
         When I enter "testing" as "powerUsername"
          And I enter "qwertz" as "powerPassword"
          And I click on "Update"
         Then I should see a "Configuration successfully saved for 1 system(s)" text
          And the cobbler report contains "Power Management Username      : testing"
          And the cobbler report contains "Power Management Password      : qwertz"
          And the cobbler report contains "Power Management Address       : 192.168.254.254"
          And the cobbler report contains "Power Management Type          : ipmitool"

    Scenario: check powermanagement SSM Operation
        Given I am on the Systems page
         When I follow "System Set Manager" in the left menu
          And I follow "power management operations" in the content area
         Then I should see this client as link
          And I should see a "Power On" button
          And I should see a "Power Off" button
          And I should see a "Reboot" button
          And I follow "Clear"

