# abstractive summarizer:
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
tokenizer = AutoTokenizer.from_pretrained("nsi319/legal-pegasus")  
model = AutoModelForSeq2SeqLM.from_pretrained("nsi319/legal-pegasus")
text = """ENGLISHIMPORTANT: BY USING YOUR APPLE WATCH, YOU ARE AGREEING TO BE BOUND BY THE 
FOLLOWING TERMS:A.     APPLE watchOS SOFTWARE LICENSE AGREEMENT
B.     APPLE PAY SUPPLEMENTAL TERMS AND CONDITIONS
C.     NOTICES FROM APPLEAPPLE INC.APPLE watchOS SOFTWARE LICENSE AGREEMENT
Single Use LicensePLEASE READ THIS SOFTWARE LICENSE AGREEMENT (ÒLICENSEÓ) CAREFULLY BEFORE USING 
YOUR APPLE WATCH OR DOWNLOADING THE SOFTWARE UPDATE ACCOMPANYING THIS 
LICENSE. BY USING YOUR APPLE WATCH OR DOWNLOADING A SOFTWARE UPDATE, AS 
APPLICABLE, YOU ARE AGREEING TO BE BOUND BY THE TERMS OF THIS LICENSE. IF YOU DO NOT AGREE TO THE TERMS OF THIS LICENSE, DO NOT USE THE APPLE WATCH OR 
DOWNLOAD THE SOFTWARE UPDATE
IF YOU HAVE RECENTLY PURCHASED AN APPLE WATCH AND YOU DO NOT AGREE TO THE 
TERMS OF THE LICENSE, YOU MAY RETURN THE APPLE WATCH WITHIN THE RETURN PERIOD 
TO THE APPLE STORE OR AUTHORIZED DISTRIBUTOR WHERE YOU OBTAINED IT FOR A 
REFUND, SUBJECT TO APPLEÕS RETURN POLICY FOUND AT 
https://www.apple.com/legal/sales-
policies/.1. General(a) The software (including Boot ROM code, embedded software and third party software), 
documentation, interfaces, content, fonts and any data that came with your Apple Watch (ÒOriginal 
watchOS SoftwareÓ), as may be updated or replaced by feature enhancements, software updates or 
system restore software provided by Apple (ÒwatchOS Software UpdatesÓ), whether in read only 
memory, on any other media or in any other form (the Original watchOS Software and watchOS Software 
Updates are collectively referred to as the ÒwatchOS SoftwareÓ) are licensed, not sold, to you by Apple 
Inc. (ÒAppleÓ) for use only under the terms of this License. Apple and its licensors retain ownership of the 
watchOS Software itself and reserve all rights not expressly granted to you. You agree that the terms of 
this License will apply to any Apple-branded app that may be pre-installed on your Apple Watch, unless 
such app is accompanied by a separate license, in which case you agree that the terms of that license 
will govern your use of that app.
(b) Apple, at its discretion, may make available future watchOS Software Updates for your Apple 
Watch.
!The watchOS Software Updates, if any, may not necessarily include all existing software features 
or new!features that Apple releases for newer or other models of Apple Watch.
! The terms of this License will govern any watchOS Software Updates provided by Apple that
!replace and/or supplement the 
Original watchOS Software
!product, unless such watchOS Software Update is
!accompanied by a separate license in which case the terms of that license will govern.
2. Permitted License Uses and Restrictions.  (a) Subject to the terms and conditions of this License, you are granted a limited non-exclusive license to 
use the watchOS Software on a single Apple Watch. Except as permitted in Section 2(b) below, and 
except as provided in a separate agreement between you and Apple, this License does not allow the 
watchOS Software to exist on more than one Apple Watch at a time, and you may not distribute or make 
the watchOS Software available over a network where it could be used by multiple devices at the same 
time. This License does not grant you any rights to use Apple proprietary interfaces and other intellectual 
property in the design, development, manufacture, licensing or distribution of third party devices and 
accessories, or third party software applications, for use with Apple Watch. Some of those rights are 
available under separate licenses from Apple. For more information on developing third party devices 
and accessories for Apple Watch, please visit 
https://developer.apple.com/programs/mÞ/
. For more 
information on developing software applications for Apple Watch, please visit 
https://developer.apple.com
.(b) Subject to the terms and conditions of this License, you are granted a limited non-exclusive license to 
download watchOS Software Updates that may be made available by Apple for your model of the Apple 
Watch to update or restore the software on any such Apple Watch that you own or control. This License 
does not allow you to update or restore any Apple Watch that you do not control or own, and you may 
not distribute or make the watchOS Software Updates available over a network where they could be 
used by multiple devices or multiple computers at the same time.(c) You may not, and you agree not to or enable others to, copy (except as expressly permitted by this 
License), decompile, reverse engineer, disassemble, attempt to derive the source code of, decrypt, 
modify, or create derivative works of the watchOS Software or any services provided by the watchOS 
Software or any part thereof (except as and only to the extent any foregoing restriction is prohibited by 
applicable law or by licensing terms governing use of open-source components that may be included 
with the watchOS Software). You agree not to remove, obscure, or alter any proprietary notices 
(including trademark and copyright notices) that may be a"xed to or contained within the watchOS Software.
(d) The watchOS Software may be used to reproduce materials so long as such use is limited to 
reproduction of non-copyrighted materials, materials in which you own the copyright, or materials you 
are authorized or legally permitted to reproduce. Notwithstanding the foregoing, you are prohibited from 
republishing, retransmitting or reproducing any images accessed through Maps (see below) as a stand-
alone Þle. Title and intellectual property rights in and to any content displayed by, stored on or accessed 
through your Apple Watch belong to the respective content owner. Such content may be protected by 
copyright or other intellectual property laws and treaties, and may be subject to terms of use of the third 
party providing such content. Except as otherwise provided herein, this License does not grant you any 
rights to use such content nor does it guarantee that such content will continue to be available to you.(e) You agree to use the watchOS Software and the Services (as deÞned in Section 5 below) in 
compliance with all applicable laws, including local laws of the country or region in which you reside or in 
which you download or use the watchOS Software and Services. Features of the watchOS Software and 
the Services may not be available in all languages or regions, some features may not be available or may 
vary based on age or region, and some may be restricted or unavailable from your service provider. A 
Bluetooth connection to a supported Apple-branded device (ÒPaired DeviceÓ) with Wi-Fi or cellular data 
connection is required for some features of the watchOS Software and Services.
(f) Use of the App Store requires a unique user name and password combination, known as an Apple ID. 
An Apple ID is also required to download apps, access app updates and certain features of the watchOS 
Software and Services. In addition, you acknowledge that many features and Services of the watchOS 
Software transmit and receive data, including app downloads and updates, and could impact charges to 
your data plan. Accordingly, you are responsible for any such charges. You can control which 
applications are permitted to use cellular data and view an estimate of how much data such applications 
have consumed under Cellular Data Settings. For more information, please consult the User Guide for 
your Apple Watch.
(g) If automatic app installs is enabled, apps on the Paired Device that also work with Apple Watch will 
automatically install and appear on the home screen of your Apple Watch. 
!You can turn o
# automatic app installs on your Apple Watch by completing the following steps: on the Paired Device, go to Watch 
App, tap General, and turn o
# Automatic App Install.If automatic app downloads is enabled, new app purchases made on Apple Watch or the
!Paired Device 
may automatically download to these devices. You can turn o
# automatic app!downloads on your Apple Watch by completing either of the following options:
!(i) on the Paired Device, go to Watch app, tap My 
Watch, tap on App
!Store, and turn o
# Automatic Downloads;!or!(ii) on your Apple Watch, go to Settings, 
tap!App Store, and turn o
# Automatic Downloads.!If automatic app updates is enabled, updates to apps on Apple!Watch or the Paired Device may 
automatically download to these devices when available.!You can turn o
# automatic app updates on your Apple Watch by completing either of the following options:
!(i) on the Paired Device, go to Watch 
app, tap My Watch, tap on App Store,
!and turn o
# Automatic Updates;!or!(ii) on your Apple Watch, go to 
Settings, tap App Store, and turn o
# Automatic!Updates.!(h) Using Apple Watch in some circumstances can distract you and may cause a dangerous situation (for 
example, avoid typing text messages while driving a car or using headphones while riding a bicycle). By using Apple Watch you agree that you are responsible for observing rules that prohibit or restrict the use 
of mobile phones or headphones (for example, the requirement to use hands-free options for making 
calls when driving).(i) Apple Watch is not a medical device and should not be used as a substitute for professional medical 
judgment. It is not designed or intended for use in the diagnosis of disease or other conditions, or in the cure, mitigation, treatment, or prevention of any condition or disease. Please consult your healthcare 
provider prior to making any decisions related to your health.
(j) Before starting or modifying any exercise program using Apple Watch, consult your physician. Be 
careful and attentive while exercising. Stop exercising immediately if you feel pain, or feel faint, dizzy, 
exhausted, or short of breath. By exercising, you assume inherent risks including any injury that may 
result from such activity.  If you have any medical condition that you believe could be a
#ected by Apple Watch (for example, seizures, blackouts, eyestrain, or headaches), consult with your physician prior to 
using Apple Watch.
(k) Subject to the terms and conditions of this License, you may use the!Memoji characters!included in or created with the Apple
!Software (ÒSystem CharactersÓ) (i) while running the Apple
!Software and (ii) to 
create your own original content and projects for your
!personal, non-commercial use.
!No other use of the System Characters is permitted by this License, including but not limited to the use,!reproduction, 
display, performance, recording, publishing or redistribution of any of the System
!Characters in a proÞt, 
non-proÞt, public
!sharing or commercial context.
!3. Transfer.
 You may not rent, lease, lend, sell, redistribute, or sublicense the watchOS Software. You 
may, however, make a one-time permanent transfer of all of your license rights to the watchOS Software 
to another party in connection with the transfer of ownership of your Apple Watch, provided that: (a) the 
transfer must include your Apple Watch and all of the watchOS Software, including all its component 
parts, and this License; (b) you do not retain any copies of the watchOS Software, full or partial, 
including copies stored on a computer or other storage device; and (c) the party receiving the watchOS 
Software reads and agrees to accept the terms and conditions of this License.
4. Consent to Use of Data.  watchOS Software features may require information from your Apple Watch 
to provide their respective functions. 
 When you turn on or use these features, details
!will be provided
!regarding what information is sent to Apple and how the information may be used.
! You can 
learn more by visiting 
https://www.apple.com/privacy/
. At all times your information will be treated in 
accordance with AppleÕs Privacy Policy, which can be viewed at: 
https://www.apple.com/legal/privacy/
.5. Services and Third Party Materials.
  (a) The watchOS Software may enable access to AppleÕs iTunes Store, App Store, iCloud, Maps, News, 
Fitness+ and other Apple and third party services and web sites (collectively and individually, ÒServicesÓ). 
Such Services may not be available in all languages or in all countries. Use of these Services requires 
Internet access and use of certain Services may require an Apple ID, and may require you to accept 
additional terms and may be subject to additional fees. By using this software in connection with an 
Apple ID, or other Apple Service, you agree to the applicable terms of service for that Service, such as 
the latest Apple Media Services Terms and Conditions for the country in which you access such 
Services, which you may access and review at 
https://www.apple.com/legal/internet-services/itunes/
.(b) If you sign up for iCloud, certain iCloud features like ÒMy Photo StreamÓ, and ÒShared AlbumsÓ may 
be accessed directly from the watchOS Software.  You acknowledge and agree that your use of iCloud 
and these features is subject to the latest terms and conditions of the iCloud service, which you may 
access and review at: 
https://www.apple.com/legal/internet-services/icloud/
.(c) Maps. The maps service and features of the watchOS Software (ÒMapsÓ), including map data 
coverage, may vary by region. When you turn on or use Maps, details will be provided regarding what 
information is sent to Apple and how the information may be used. Certain information will be processed 
by Apple in accordance with AppleÕs Privacy Policy. For more information, visit 
www.apple.com/legal/
privacy/data/en/apple-maps. You can disable the location-based functionality of Maps
!by going to!Settings > Privacy > Location Services > Maps on the Paired Device
!or, if using the Apple Watch 
through Family Setup,
!using!the watchOS Software. Certain Maps features will be unavailable if you 
disable this setting.!You acknowledge and agree that your use of Maps is subject to the latest terms and 
conditions of the Map service, which you may access and review by scrolling to the bottom of the 
screen when you use Maps on your Apple Watch.
(d) You understand that by using any of the Services, you may encounter content that may be deemed 
o#ensive, indecent, or objectionable, which content may or may not be identiÞed as having explicit language, and that the results of any search may automatically and unintentionally generate links or 
references to objectionable material. Nevertheless, you agree to use the Services at your sole risk and 
that Apple, its a"liates, agents, principals, or licensors shall have no liability to you for content that may be found to be o#ensive, indecent, or objectionable.(e) Certain Services may display, include or make available content, data, information, applications or 
materials from third parties (ÒThird Party MaterialsÓ) or provide links to certain third party web sites. By 
using the Services, you acknowledge and agree that Apple is not responsible for examining or evaluating 
the content, accuracy, completeness, timeliness, validity, copyright compliance, legality, decency, quality 
or any other aspect of such Third Party Materials or web sites. Apple, its o
"cers, a"liates and subsidiaries do not warrant or endorse and do not assume and will not have any liability or responsibility 
to you or any other person for any third-party Services, Third Party Materials or web sites, or for any 
other materials, products, or services of third parties. Third Party Materials and links to other web sites 
are provided solely as a convenience to you.
(f) Neither Apple nor any of its content providers guarantees the availability, accuracy, completeness, 
reliability, or timeliness of stock information, location data or any other data displayed by any Services.  
Financial information displayed by any Services is for general informational purposes only and should not be relied upon as investment advice. Before executing any securities transaction based upon 
information obtained through the Services, you should consult with a Þnancial or securities professional 
who is legally qualiÞed to give Þnancial or securities advice in your country or region. Location data 
provided by any Services, including the Apple Maps service, is provided for basic navigational and/or 
planning purposes only and is not intended to be relied upon in situations where precise location 
information is needed or where erroneous, inaccurate, time-delayed or incomplete location data may 
lead to death, personal injury, property or environmental damage. You agree that the results you receive 
from the Maps service may vary from actual road or terrain conditions due to factors that can a
#ect the accuracy of the Maps data, such as, but not limited to, weather, road and tra
"c conditions, and geopolitical events. For your safety when using the navigation feature, always pay attention to
!posted road signs and current road conditions. Follow safe driving practices and tra
"c regulations, and note 
that cycling and walking directions may not include designated pathways.
(g) To the extent that you upload any content through the use of the Services, you represent that you 
own all rights in, or have authorization or are otherwise legally permitted to upload, such content and 
that such content does not violate any terms of service applicable to the Services. You agree that the 
Services contain proprietary content, information and material that is owned by Apple, the site owner 
and/or their licensors, and is protected by applicable intellectual property and other laws, including but 
not limited to copyright. You agree that you will not use such proprietary content, information or 
materials other than for permitted use of the Services or in any manner that is inconsistent with the terms of this License or that infringes any intellectual property rights of a third party or Apple. No portion 
of the Services may be reproduced in any form or by any means. You agree not to modify, rent, lease, 
loan, sell, distribute, or create derivative works based on the Services, in any manner, and you shall not 
exploit the Services in any unauthorized way whatsoever, including but not limited to, using the Services 
to transmit any computer viruses, worms, trojan horses or other malware, or by trespass or burdening 
network capacity. You further agree not to use the Services in any manner to harass, abuse, stalk, 
threaten, defame or otherwise infringe or violate the rights of any other party, and that Apple is not in any 
way responsible for any such use by you, nor for any harassing, threatening, defamatory, o
#ensive, infringing or illegal messages or transmissions that you may receive as a result of using any of the 
Services.(h) In addition, Services and Third Party Materials that may be accessed, linked to or displayed on the 
Apple Watch are not available in all languages or in all countries or regions. Apple makes no 
representation that such Services and Third Party Materials are appropriate or available for use in any 
particular location. To the extent you choose to use or access such Services and Third Party Materials, 
you do so at your own initiative and are responsible for compliance with any applicable laws, including 
but not limited to applicable local laws and privacy and data collection laws. Sharing or syncing photos through your Apple Watch may cause metadata, including photo location data, to be transmitted with 
the photos. Apple and its licensors reserve the right to change, suspend, remove, or disable access to 
any Services at any time without notice. In no event will Apple be liable for the removal of or disabling of 
access to any such Services. Apple may also impose limits on the use of or access to certain Services, in any case and without notice or liability6. Termination.
 This License is e#ective until terminated. Your rights under this License will terminate 
automatically or otherwise cease to be e#ective without notice from Apple if you fail to comply with any 
term(s) of this License. Upon the termination of this License, you shall cease all use of the watchOS Software.  Sections 4, 5, 6, 7, 8, 11 and 12 of this License shall survive any such termination.
7. Disclaimer of Warranties
7.1     If you are a customer who is a consumer (someone who uses the watchOS Software outside of 
your trade, business or profession), you may have legal rights in your country of residence which would 
prohibit the following limitations from applying to you, and where prohibited they will not apply to you. To 
Þnd out more about rights, you should contact a local consumer advice organization.
7.2     YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT, TO THE EXTENT PERMITTED BY 
APPLICABLE LAW, USE OF THE watchOS SOFTWARE AND ANY SERVICES PERFORMED BY OR 
ACCESSED THROUGH THE watchOS SOFTWARE IS AT YOUR SOLE RISK AND THAT THE ENTIRE 
RISK AS TO SATISFACTORY QUALITY, PERFORMANCE, ACCURACY AND EFFORT IS WITH YOU.
7.3     TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THE watchOS SOFTWARE AND 
SERVICES ARE PROVIDED ÒAS ISÓ AND ÒAS AVAILABLEÓ, WITH ALL FAULTS AND WITHOUT 
WARRANTY OF ANY KIND, AND APPLE AND APPLEÕS LICENSORS (COLLECTIVELY REFERRED TO 
AS ÒAPPLEÓ FOR THE PURPOSES OF SECTIONS 7 AND 8) HEREBY DISCLAIM ALL WARRANTIES 
AND CONDITIONS WITH RESPECT TO THE watchOS SOFTWARE AND SERVICES, EITHER EXPRESS, 
IMPLIED OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES AND/OR 
CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR 
PURPOSE, ACCURACY, QUIET ENJOYMENT, AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS.
7.4     APPLE DOES NOT WARRANT AGAINST INTERFERENCE WITH YOUR ENJOYMENT OF THE 
watchOS SOFTWARE AND SERVICES, THAT THE FUNCTIONS CONTAINED IN, OR SERVICES 
PERFORMED OR PROVIDED BY, THE watchOS SOFTWARE WILL MEET YOUR REQUIREMENTS, THAT 
THE OPERATION OF THE watchOS SOFTWARE AND SERVICES WILL BE UNINTERRUPTED OR 
ERROR-FREE, THAT ANY SERVICE WILL CONTINUE TO BE MADE AVAILABLE, THAT DEFECTS IN THE 
watchOS SOFTWARE OR SERVICES WILL BE CORRECTED, OR THAT THE watchOS SOFTWARE WILL 
BE COMPATIBLE OR WORK WITH ANY THIRD PARTY SOFTWARE, APPLICATIONS OR THIRD PARTY 
SERVICES. INSTALLATION OF THIS watchOS SOFTWARE MAY AFFECT THE AVAILABILITY AND 
USABILITY OF THIRD PARTY SOFTWARE, APPLICATIONS OR THIRD PARTY SERVICES, AS WELL AS 
APPLE PRODUCTS AND SERVICES.
7.5     YOU FURTHER ACKNOWLEDGE THAT THE watchOS SOFTWARE AND SERVICES ARE NOT 
INTENDED OR SUITABLE FOR USE IN SITUATIONS OR ENVIRONMENTS WHERE THE FAILURE OR 
TIME DELAYS OF, OR ERRORS OR INACCURACIES IN, THE CONTENT, DATA OR INFORMATION 
PROVIDED BY THE watchOS SOFTWARE OR SERVICES COULD LEAD TO DEATH, PERSONAL 
INJURY, OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE, INCLUDING WITHOUT LIMITATION 
THE OPERATION OF NUCLEAR FACILITIES, AIRCRAFT NAVIGATION OR COMMUNICATION 
SYSTEMS, AIR TRAFFIC CONTROL, LIFE SUPPORT OR WEAPONS SYSTEMS.
7.6     NO ORAL OR WRITTEN INFORMATION OR ADVICE GIVEN BY APPLE OR AN APPLE 
AUTHORIZED REPRESENTATIVE SHALL CREATE A WARRANTY. SHOULD THE watchOS SOFTWARE 
OR SERVICES PROVE DEFECTIVE, YOU ASSUME THE ENTIRE COST OF ALL NECESSARY 
SERVICING, REPAIR OR CORRECTION. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF 
IMPLIED WARRANTIES OR LIMITATIONS ON APPLICABLE STATUTORY RIGHTS OF A CONSUMER, 
SO THE ABOVE EXCLUSION AND LIMITATIONS MAY NOT APPLY TO YOU.
8. Limitation of Liability. 
TO THE EXTENT NOT PROHIBITED BY APPLICABLE LAW, IN NO EVENT 
SHALL APPLE, ITS AFFILIATES, AGENTS OR PRINCIPALS BE LIABLE FOR PERSONAL INJURY, OR 
ANY INCIDENTAL, SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES WHATSOEVER, INCLUDING, 
WITHOUT LIMITATION, DAMAGES FOR LOSS OF PROFITS, CORRUPTION OR LOSS OF DATA, 
FAILURE TO TRANSMIT OR RECEIVE ANY DATA (INCLUDING WITHOUT LIMITATION COURSE 
INSTRUCTIONS, ASSIGNMENTS AND MATERIALS), BUSINESS INTERRUPTION OR ANY OTHER 
COMMERCIAL DAMAGES OR LOSSES, ARISING OUT OF OR RELATED TO YOUR USE OR INABILITY 
TO USE THE watchOS SOFTWARE AND SERVICES OR ANY THIRD PARTY SOFTWARE, 
APPLICATIONS OR SERVICES IN CONJUNCTION WITH THE watchOS SOFTWARE OR SERVICES, 
HOWEVER CAUSED, REGARDLESS OF THE THEORY OF LIABILITY (CONTRACT, TORT OR 
OTHERWISE) AND EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 
SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OR LIMITATION OF LIABILITY FOR 
PERSONAL INJURY, OR OF INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THIS LIMITATION MAY 
NOT APPLY TO YOU. In no event shall AppleÕs total liability to you for all damages (other than as may be 
required by applicable law in cases involving personal injury) exceed the amount of two hundred and Þfty 
dollars (U.S.$250.00). The foregoing limitations will apply even if the above stated remedy fails of its 
essential purpose.9. Export Control. 
You may not use or otherwise export or re-export the watchOS Software except as 
authorized by United States law and the laws of the jurisdiction(s) in which the watchOS Software was 
obtained. In particular, but without limitation, the watchOS Software may not be exported or re-exported 
(a) into any U.S. embargoed countries or (b) to anyone on the U.S. Treasury DepartmentÕs list of Specially 
Designated Nationals or the U.S. Department of Commerce Denied PersonÕs List or Entity List or any 
other restricted party lists. By using the watchOS Software, you represent and warrant that you are not 
located in any such country or on any such list. You also agree that you will not use the watchOS 
Software for any purposes prohibited by United States law, including, without limitation, the 
development, design, manufacture or production of missiles, nuclear, chemical or biological weapons.
10. Government End Users. 
The watchOS Software and related documentation are ÒCommercial 
ItemsÓ, as that term is deÞned at 48 C.F.R. ¤2.101, consisting of ÒCommercial Computer SoftwareÓ and 
ÒCommercial Computer Software DocumentationÓ, as such terms are used in 48 C.F.R. ¤12.212 or 48 
C.F.R. ¤227.7202, as applicable. Consistent with 48 C.F.R. ¤12.212 or 48 C.F.R. ¤227.7202-1 through 
227.7202-4, as applicable, the Commercial Computer Software and Commercial Computer Software 
Documentation are being licensed to U.S. Government end users (a) only as Commercial Items and (b) 
with only those rights as are granted to all other end users pursuant to the terms and conditions herein. 
Unpublished-rights reserved under the copyright laws of the United States.
11. Controlling Law and Severability.
 This License will be governed by and construed in accordance 
with the laws of the State of California, excluding its conßict of law principles. This License shall not be 
governed by the United Nations Convention on Contracts for the International Sale of Goods, the 
application of which is expressly excluded. If you are a consumer based in the United Kingdom, this 
License will be governed by the laws of the jurisdiction of your residence.  If for any reason a court of 
competent jurisdiction Þnds any provision, or portion thereof, to be unenforceable, the remainder of this 
License shall continue in full force and e
#ect.  12. Complete Agreement; Governing Language.
 This License constitutes the entire agreement 
between you and Apple relating to the watchOS Software and supersedes all prior or contemporaneous 
understandings regarding such subject matter. No amendment to or modiÞcation of this License will be 
binding unless in writing and signed by Apple. Any translation of this License is done for local requirements and in the event of a dispute between the English and any non-English versions, the 
English version of this License shall govern, to the extent not prohibited by local law in your jurisdiction.
13. Third Party Acknowledgements. 
Portions of the watchOS Software may utilize or include third 
party software and other copyrighted material. Acknowledgements, licensing terms and disclaimers for 
such material are contained in the electronic documentation for the watchOS Software, and your use of 
such material is governed by their respective terms
EA17777/16/2021ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑApple Pay & Wallet Supplemental Terms and Conditions
These Apple Pay & Wallet Supplemental Terms and Conditions (these ÒSupplemental TermsÓ) 
supplement the Apple watchOS Software License Agreement (the ÒLicenseÓ); both the terms of the 
License and these Supplemental Terms govern your use of the Apple Pay feature (ÒApple PayÓ) and 
Apple Wallet application (ÒWalletÓ) on your Apple Watch, which shall be deemed a ÒServiceÓ under the 
License. Capitalized terms used in these Supplemental Terms have the meanings set forth in the 
License.1.     OverviewApple PayApple Pay allows you to:$     make contactless payments using credit, debit, and prepaid cards, including Apple Card and 
the Apple Cash card, in select locations, or within select apps or websites; and
$     send person to person payments to other Apple Cash users.Apple Pay and certain features of Apple Pay may only be available in select regions, with select card 
issuers, payment networks, merchants, and other third parties. 
Wallet
Apple Wallet allows you to store virtual representations of credit, debit, and prepaid cards to be used 
with Apple Pay (collectively, ÒApple Pay CardsÓ), as well as other types of cards, passes, and keys, 
including without limitation the following (collectively, ÒWallet PassesÓ, and together with Apple Pay 
Cards, the ÒSupported CardsÓ):
$      rewards cards;
$      transit cards; 
$      tickets; $      membership passes;$      car keys; $      home keys;$      hospitality keys;$      corporate badges; $      student ID cards; and
$      driverÕs license and state or government-issued identiÞcation cards (ÒID CardsÓ).
Wallet Passes may only be available in select regions and with select partners. ID Cards may only be 
available for residents of participating states and presentment may vary by state or location. 
 Supported Cards may change from time to time.
2.     Eligibility To use Apple Pay and Wallet, you must have (i) a supported Apple Watch running a version of operating 
software that supports the Services (latest version recommended and sometimes required), (ii) an Apple 
ID associated with an iCloud account that is in good standing with Apple, and (iii) Internet access (fees 
may apply). With the exception of Apple Cash Family and select e-money cards, Apple Pay Cards are 
only available to individuals aged 13 years or older, and may be subject to additional age-based 
restrictions imposed by iCloud or the relevant issuer, merchant, or other third party.
If you are a parent or legal guardian of an iCloud Family (an ÒOrganizerÓ), you may invite Family 
members, including those under age 13 (or the equivalent minimum age in the applicable country), to provision and use eligible transit cards in Wallet. As the Organizer, you will be responsible for all 
payments, purchases, and transactions made using the transit card that has been enabled for Family 
members, including those initiated by the Family member. Eligibility for, and use of, transit cards in Wallet 
are subject to the terms and conditions of the relevant transit agency. Organizers are responsible for 
complying with such terms and conditions and assume all risk related to enabling transit passes with 
other Family members. When a Family member leaves or is removed from the Family, the Family 
member will no longer be able to reload the transit card and will only be able to transact on the card until 
such time as the card account balance is zero. 
 If you are the owner of a car key, you can share your car key with others aged 13 years or older so they 
can unlock, access, and/or drive your car. 
 Home keys can only be added or removed from Wallet by adding or removing locks in the Home app or 
adding or removing yourself from a home in the Home app. If you are the administrator of a home in the 
Home app, any existing home keys will automatically be shared with people whom you have invited and 
who join your Home. Apple Card is only available in the United States and is issued by Goldman Sachs Bank USA, Salt Lake 
City Branch (ÒApple Card IssuerÓ). With the exception of Apple Card Family, Apple Card is only available 
to individuals aged 18 years or older (or older depending on your state of residence). 
 The Apple Cash card and the ability to send and receive person to person payments are only available in 
the United States, and are services provided by Green Dot Bank, member FDIC. In order to send or 
receive person to person payments in Apple Pay, you must have an Apple Cash card. With the exception 
of Apple Cash Family, the Apple Cash card and the ability to send and receive person to person 
payments are only available to individuals aged 18 years or older.
3.     Use of the Services Supported Cards and person to person payments are associated with the Apple ID you have signed into 
iCloud to use these features. When you add or remove keys, corporate badges, rewards cards, tickets 
and membership passes in Wallet, the change may appear on your other Apple devices where you are 
signed in with your Apple ID. You will only be able to associate one ID Card for each state issuing 
authority with each Apple ID.  Apple Pay and Wallet are intended for your personal use and you may only provision your own 
Supported Cards or those transit cards or car and home keys that you have been invited to provision 
from an Organizer or owner. If you are provisioning a supported corporate card, you represent that you 
are doing so with the authorization of your employer and you are authorized to bind your employer to 
these terms of use and all transactions e#ected by use of this feature. If you are sending or receiving a 
person to person payment, you represent that you are doing so for your own personal, non-commercial 
use. If you are provisioning an ID Card, you represent that you are doing so using your own personal 
information that accurately and truthfully represents you.
You agree not to use Apple Pay or Wallet for illegal or fraudulent purposes, or any other purposes which 
are prohibited by the License and these Supplemental Terms. You further agree to use Apple Pay and 
Wallet in accordance with applicable laws and regulations. You acknowledge that any false information 
submitted in connection with an ID Card may be a criminal o
#ense under federal or state law. You agree 
not to interfere with or disrupt the Apple Pay or Wallet service (including accessing the service through 
any automated means), or any servers or networks connected to the service, or any policies, requirements, or regulations of networks connected to the service (including any unauthorized access to, 
use, or monitoring of data or tra"c thereon).
If your access to or use of Apple Pay or Wallet is prohibited by applicable law, you are not authorized to 
access or use these Services. We are not responsible if you access or use the Services in any manner 
that violates applicable law.
4.     AppleÕs Relationship With You
Your use of Apple Pay will be governed by these Supplemental Terms, as well as by the terms of the 
cardholder agreement you have in place with the relevant issuer, merchant, or other third party 
responsible for your Apple Pay Card.
 Similarly, your use of Wallet Passes in Wallet will be governed by these Supplemental Terms, as well as 
by the terms of your agreement with the relevant merchant, transit agency, car and lock manufacturer, 
university, hotel, resort, corporation, state issuing authority, or other third party.
 With the exception of certain features of Apple Pay provided by Apple Payments Inc. (ÒApple 
PaymentsÓ) described below, Apple does not process payments or other non-payment transactions 
made on your Apple Pay Cards . Apple has no control over, and is not responsible for, any payments, 
chargebacks, returns, refunds, rewards, value, discounts, access, identity veriÞcation, or other activity 
that may arise out of your use of Apple Pay or Wallet.
If there is any conßict between the terms of these Supplemental Terms and your agreement with the 
relevant issuer, merchant, state issuing authority, or other third party (each, a Ò
Third Party Agreement
Ó), the terms of these Supplemental Terms will govern your relationship with Apple, and the terms of the 
relevant Third Party Agreement will govern your relationship with such third party.
You agree that Apple is not a party to any of your Third Party Agreements, nor is Apple responsible for: 
(a) the content, accuracy or availability of any Supported Cards, purchases, transactions, or other 
activities while using Apple Pay or Wallet, including without limitation those made by Family members or 
others with whom you have shared your Supported Cards; (b) the issuance of credit or accessing 
eligibility for credit; (c) the issuance, suspension or revocation of a driverÕs license or state identiÞcation 
card; (d) provisioning decisions made by an issuer, merchant, or other third party in connection with 
adding your Supported Card to Wallet; (e) your membership or participation in any merchant or partner 
program; (f) any accrual or redemption of rewards or stored value in connection with your Supported 
Cards; (g) funding or reloading of prepaid Supported Cards; (h) sending or receiving of person to person 
payments; or (i) loading, redeeming, or withdrawing money from your Apple Cash card.
When you apply for Apple Card, you are applying to open an account with the Apple Card Issuer. The 
Þnancial institution responsible for o
#ering Apple Card is subject to change, and your use of Apple Card 
is subject to their terms and conditions.When you enable the Apple Cash features within Apple Pay, you are opening an account with Green Dot 
Bank. With the exception of the features of Apple Pay provided by Apple Payments, when you send or 
receive a person to person payment or load or withdraw money from your Apple Cash card, Green Dot 
Bank will be responsible for receiving and sending your money to the intended recipient. The Þnancial 
institution responsible for o
#ering Apple Cash and person to person payments within Apple Pay is subject to change, and your use of such features are subject to their terms and conditions.
The ability to use funds in your Apple Cash card to make payments to certain eligible businesses that 
you authorized (the ÒDirect Payments ServiceÓ) is a service provided by Apple Payments. Your use of the 
Direct Payments Service is subject to Apple PaymentsÕ Direct Payments Terms and Conditions. 
Additionally, certain eligible businesses may allow you to authorize them to disburse funds to your Apple 
Cash card (each, a ÒDisbursementÓ). While Disbursements may be processed by Apple Payments, they 
are o
#ered by the participating businesses that provide such funds and may be subject to certain 
additional terms and conditions of the disbursing businesses.For all disputes or questions about Supported Cards or associated commerce activity, please contact 
your issuer or the applicable merchant, state issuing authority, or other third party. For questions 
regarding Apple Pay, Wallet, Apple Card or the Apple Cash card or person to person payments, please 
contact Apple Support.5.     PrivacyAppleÕs collection and use of personal information is governed by the Apple Privacy Policy, available at 
https://www.apple.com/legal/privacy/en-ww/
. You can Þnd detailed information on the personal 
information collected, used, or shared as part of your use of Apple Pay 
and Wallet 
by reading the 
relevant service speciÞc privacy notices, including About Apple Pay and Privacy, which can be accessed 
within the Watch app on a Paired Device, or by visiting  
https://www.apple.com/legal/privacy/en-ww/
. By using Apple Pay and Wallet, you agree and consent to AppleÕs and its subsidiariesÕ and agentsÕ 
transmission, collection, maintenance, processing, and use of all of the foregoing information, to provide 
these Services6.     Security; Lost or Disabled DevicesPROTECTING YOUR APPLE WATCH AND CREDENTIALS LIKE YOU WOULD PROTECT YOUR 
PHYSICAL WALLET AND CARDS 
Apple Pay and Wallet store virtual representations of your Supported Cards and should be protected as 
you would protect your physical wallet, keys, or credit, debit, prepaid, identity and other cards. You are 
solely responsible for maintaining the security of your Apple Watch and your Apple ID, the passcode to 
your Apple Watch, and any other authentication credentials used in connection with the Services 
(collectively, your ÒCredentialsÓ). If you authorize or allow anyone else to use your Apple Watch (
e.g., by providing your device passcode to a third party or otherwise providing any of your Credentials to a third 
party), the person may be able to make payments, send, request, or receive person to person payments, 
withdraw money from your Apple Cash card, receive or redeem rewards, use value, unlock, or otherwise 
access your car, room, o
"ce or home, impersonate your identity, or make other transactions with your 
Supported Cards in Wallet. In such event, you will be responsible for all payments, access and 
transactions made by that person.JAILBROKEN DEVICESIf you make unauthorized modiÞcations to your Apple Watch, such as by disabling hardware or software 
controls (sometimes referred to as ÒjailbreakingÓ), your device may no longer be eligible to access or use 
the Services. You acknowledge that the use of a modiÞed device in connection with the Services is 
expressly prohibited, constitutes a violation of these Supplemental Terms, and is grounds for us to deny 
or limit your access to the Services.ADDITIONAL SECURITY MEASURES You may need to enable additional security measures, such as two-factor authentication for your Apple 
ID, in order to access particular features of Apple Pay, including Apple Card, the Apple Cash card, and 
person to person payments with Apple Pay. If you subsequently remove those security features, you 
may not be able to continue to access particular features of Apple Pay.
LOST OR STOLEN DEVICES If your Apple Watch is lost or stolen and you have Find My iPhone enabled, you can use Find My iPhone 
to attempt to suspend the ability to transact with the virtual Supported Cards or sending person to 
person payments on that device by putting it into Lost Mode. If your Apple Watch is in Lost Mode, your 
car key may be disabled in Wallet and you will no longer be able to access or start your car once you 
have left the vehicle or turned o
# the engine. Lost mode only a#ects keys on the lost device. If you are 
the owner, you will no longer be able to share your car key or home key with others, but keys that have 
already been shared with others will not be impacted from their Apple devices.
You can also erase your device, which will attempt to suspend the ability to transact with the virtual 
Supported Cards or send person to person payments on the device. You should also contact the issuer, 
merchant, or other responsible third party of your Supported Cards, or Apple in the case of your Apple 
Card or Apple Cash card, 
in order to prevent unauthorized access to your Supported Cards
 on Apple Pay and in Wallet
.If you report or Apple suspects fraudulent or abusive activity, you agree to cooperate with Apple in any 
investigation and to use any fraud prevention measures we prescribe.
7.     Limitation of LiabilityIN ADDITION TO THE DISCLAIMERS OF WARRANTIES AND LIMITATION OF LIABILITY SET FORTH IN 
THE LICENSE, APPLE DOES NOT ASSUME ANY LIABILITY FOR PURCHASES, PAYMENTS, ACCESS, 
IDENTITY VERIFICATION, TRANSACTIONS, OR OTHER ACTIVITY MADE USING APPLE PAY OR 
WALLET, AND YOU AGREE TO LOOK SOLELY TO AGREEMENTS YOU MAY HAVE WITH YOUR CARD 
ISSUER, PAYMENT NETWORK, FINANCIAL INSTITUTIONS, MERCHANT, STATE ISSUING AUTHORITY, 
OR OTHER APPLICABLE THIRD PARTY TO RESOLVE ANY QUESTIONS OR DISPUTES RELATING TO 
YOUR SUPPORTED CARDS, PERSON TO PERSON PAYMENTS, AND ASSOCIATED ACTIVITIES.
ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑNOTICES FROM APPLEIf Apple needs to contact you about your product or account, you consent to receive the notices by 
email. You agree that any such notices that we send you electronically will satisfy any legal 
communication requirements.
"""
chars_so_far = ""
summaries = []
for chars in text:
    chars_so_far += chars
    if len(chars_so_far) > 1023:
      input_tokenized = tokenizer.encode(chars_so_far, return_tensors='pt',max_length=1024,truncation=True)
      summary_ids = model.generate(input_tokenized,
                                        num_beams=9,
                                        no_repeat_ngram_size=3,
                                        length_penalty=2.0,
                                        min_length=150,
                                        max_length=2500,
                                        early_stopping=True)
      summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
      print(summary)
      summaries.append(summary)
      chars_so_far = ""
if chars_so_far != "":
  input_tokenized = tokenizer.encode(chars_so_far, return_tensors='pt',max_length=1024,truncation=True)
  summary_ids = model.generate(input_tokenized,
                                    num_beams=9,
                                    no_repeat_ngram_size=3,
                                    length_penalty=2.0,
                                    min_length=150,
                                    max_length=2500,
                                    early_stopping=True)
  summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
  print(summary)
  summaries.append(summary)