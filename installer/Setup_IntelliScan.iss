#define MyAppName "Sigma Controls - IntelliScan v1.4"
#define MyAppVersion "1.4.0"
#define MyAppPublisher "Sigma Controls"
#define MyAppURL "https://www.sigmacontrolsindia.com/"
#define MyAppExeName "Sigma Controls - IntelliScan v1.4.exe"

[Setup]
AppId={{5D4BF946-16D9-4C97-A4AC-F33680230693}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
AppVerName=Sigma Controls - IntelliScan v1.4
AppComments=Industrial Multi-Parameter Data Acquisition & Monitoring Software
DefaultDirName={userdocs}\Sigma Controls\Sigma Controls - IntelliScan v1.4
DisableDirPage=no
UsePreviousAppDir=no
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
DefaultGroupName=Sigma Controls
LicenseFile=D:\Finally\Sigma_Scanner_3.1\License.txt
InfoBeforeFile=D:\Finally\Sigma_Scanner_3.1\Beginning Details.txt
InfoAfterFile=D:\Finally\Sigma_Scanner_3.1\Ending Details.txt
OutputDir=D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.4
OutputBaseFilename=Sigma Controls IntelliScan v1.4 Installer
SetupIconFile=D:\Finally\Sigma_Scanner_3.1\SIGMA_ICON.ico
Password=SC15
Encryption=yes
Compression=lzma2
SolidCompression=yes
LZMANumBlockThreads=4
WizardStyle=modern
WizardImageFile=D:\Finally\Sigma_Scanner_3.1\wizard.bmp
WizardImageStretch=yes
PrivilegesRequired=admin
VersionInfoCompany=Sigma Controls
VersionInfoProductName=Sigma Controls - IntelliScan v1.4
VersionInfoProductVersion=1.4.0
VersionInfoVersion=1.4.0.0
VersionInfoDescription=Industrial Multi-Parameter Data Acquisition & Monitoring Software
VersionInfoCopyright=© 2026 Sigma Controls
UninstallDisplayIcon={app}\SIGMA_ICON.ico
UninstallDisplayName=Sigma Controls - IntelliScan v1.4

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\config.json"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\credentials.json"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "D:\Finally\Sigma_Scanner_3.1\SIGMA_ICON.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\Sigma Controls License Installer.exe"; DestDir: "{app}"; Flags: ignoreversion deleteafterinstall

; --- NEW FILES FOR THE UPDATER ---
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\Sigma Controls - IntelliScan Updater.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Finally\Sigma_Scanner_3.1\Sigma Controls - IntelliScan v1.1\version.json"; DestDir: "{app}"; Flags: ignoreversion
; ---------------------------------

[Icons]
Name: "{group}\IntelliScan"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\Sigma Controls License Installer.exe"; Flags: waituntilterminated; StatusMsg: "Activating Sigma Controls License..."
Filename: "{app}\{#MyAppExeName}"; Description: "Launch Sigma Controls IntelliScan"; Flags: nowait postinstall skipifsilent

[Code]

var
  GFreshInstall: Boolean;

function GetPhysicalMac(): String;
var
  ResultCode: Integer;
  TempFile: String;
  Content: AnsiString;
  PSCommand: String;
begin
  Result := '';
  TempFile := ExpandConstant('{tmp}\sigma_mac.txt');

  PSCommand :=
    'powershell.exe -ExecutionPolicy Bypass -NoProfile -Command ' +
    '"$mac = (Get-NetAdapter | Where-Object { ' +
    '$_.Status -eq ''Up'' -and ' +
    '($_.PhysicalMediaType -eq ''802.3'' -or $_.PhysicalMediaType -eq ''Native 802.11'') ' +
    '} | Sort-Object -Property LinkSpeed -Descending | ' +
    'Select-Object -First 1 -ExpandProperty MacAddress); ' +
    'if ($mac) { $mac.ToLower() -replace ''-'','':'' } else { '''' }"' +
    ' > "' + TempFile + '" 2>&1';

  Exec(
    ExpandConstant('{cmd}'),
    '/C ' + PSCommand,
    '',
    SW_HIDE,
    ewWaitUntilTerminated,
    ResultCode
  );

  if ResultCode <> 0 then
  begin
    Log('GetPhysicalMac: PowerShell exited with code ' + IntToStr(ResultCode));
    Exit;
  end;

  Content := '';
  LoadStringFromFile(TempFile, Content);

  if Content = '' then
  begin
    Log('GetPhysicalMac: Failed to read temp file or file empty: ' + TempFile);
    DeleteFile(TempFile);
    Exit;
  end;

  Content := Trim(Content);

  if Length(Content) <> 17 then
  begin
    Log('GetPhysicalMac: Unexpected MAC format: [' + Content + ']');
    Result := '';
  end
  else
    Result := Content;

  DeleteFile(TempFile);
end;


function NextButtonClick(CurPageID: Integer): Boolean;
var
  CredFile: String;
begin
  Result := True;
  if CurPageID = wpReady then
  begin
    CredFile := ExpandConstant('{app}\credentials.json');
    GFreshInstall := not FileExists(CredFile);
    if GFreshInstall then
      Log('NextButtonClick: GFreshInstall = True')
    else
      Log('NextButtonClick: GFreshInstall = False');
  end;
end;


procedure UpdateCredentialsFile();
var
  FileName: String;
  MacAddr: String;
  JsonContent: String;
begin
  if not GFreshInstall then
  begin
    Log('UpdateCredentialsFile: Upgrade detected, skipping.');
    Exit;
  end;

  FileName := ExpandConstant('{app}\credentials.json');

  if not FileExists(FileName) then
  begin
    Log('UpdateCredentialsFile: credentials.json not found. Aborting.');
    Exit;
  end;

  MacAddr := GetPhysicalMac();

  if MacAddr = '' then
  begin
    Log('UpdateCredentialsFile: MAC detection failed. Writing with empty MAC.');
    MsgBox(
      'Warning: Could not detect a physical network adapter MAC address.' + #13#10 +
      'The software may require re-activation after installation.' + #13#10 +
      'Please contact Sigma Controls support if this issue persists.',
      mbInformation,
      MB_OK
    );
  end;

  JsonContent :=
    '{' + #13#10 +
    '  "users": [' + #13#10 +
    '    {' + #13#10 +
    '      "id": "SigmaControls",' + #13#10 +
    '      "password": "SC15",' + #13#10 +
    '      "mac": "' + MacAddr + '"' + #13#10 +
    '    }' + #13#10 +
    '  ]' + #13#10 +
    '}';

  if not SaveStringToFile(FileName, JsonContent, False) then
  begin
    Log('UpdateCredentialsFile: Failed to write credentials.json');
    MsgBox(
      'Error: Could not write credentials file.' + #13#10 +
      'Please ensure the installation directory is writable.' + #13#10 +
      'Path: ' + FileName,
      mbError,
      MB_OK
    );
  end
  else
    Log('UpdateCredentialsFile: Successfully written with MAC: ' + MacAddr);
end;


procedure HideFiles();
var
  ResultCode: Integer;
begin
  Exec(
    ExpandConstant('{cmd}'),
    '/C attrib +H "' + ExpandConstant('{app}\credentials.json') + '"',
    '',
    SW_HIDE,
    ewWaitUntilTerminated,
    ResultCode
  );
  if ResultCode <> 0 then
    Log('HideFiles: Failed to hide credentials.json: ' + IntToStr(ResultCode))
  else
    Log('HideFiles: credentials.json hidden.');
end;


procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    Log('CurStepChanged: ssPostInstall reached.');
    UpdateCredentialsFile();
    HideFiles();
  end;
end;


// Fires at the very last moment before setup process exits —
// the only safe place to delete the running setup exe itself.
procedure DeinitializeSetup();
var
  ResultCode: Integer;
begin
  Exec(
    ExpandConstant('{cmd}'),
    '/C choice /C Y /N /D Y /T 5 >NUL & del /F /Q "' + ExpandConstant('{srcexe}') + '"',
    '',
    SW_HIDE,
    ewNoWait,
    ResultCode
  );
  Log('DeinitializeSetup: Self-delete command launched for: ' + ExpandConstant('{srcexe}'));
end;
