<#
  Script Name:                  Challenge1-ADUser
  Class Name:                   Ops 301
  Author Name:                  Cody Wishart
  Date of latest revision:      3/10/21
  Purpose:                      Add a new AD user 
#>

New-ADUser -Name "Franz Ferdinand" -Office "Springfield, OR" -OtherAttributes @{ 'title'="TPS Reporting Lead";
                                                                                 'mail'="ferdi@GlobeXpower.com";
                                                                                 'company'="GlobeX USA";
                                                                                 'department'="TPS"
                                                                                  }
