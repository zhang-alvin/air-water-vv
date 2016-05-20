
function [Pxx,kz] = powerspec(x,nfft,dz,window)
% POWER SPECTRUM -- Power/variance spectrum
% =========================================================================
%
%   FORMAT:     [Pxx,kz] = powerspec(x,dz,window)
%
%   IN:         fn      signal f(z)     [1xN]
%               dz      sampling period [1x1]
%               window  window switch   1=boxcar, 2=10%sin^2
% 
% =========================================================================

N=length(x);                       % length of data vector
% define window
if window==1 % boxcar
    w=ones(N,1);
elseif window==2 % 10% sin^2 window
    w=ones(N,1);
    ifrac=ceil(0.1*N);  
    index=1:ifrac; % first 10% 
    w(index)=sin(pi/2*index/ifrac).^2; clear index
    index=N-ifrac+1:N; % last 10%
    w(index)=sin(pi/2*(index-N-1)/ifrac).^2;
elseif window==3 % Hann window
    w=0.5*(1-cos(2*pi*[0:N-1]'/(N-1)));
else
    error('window identifier invalid');
end
% power spectrum
%nfft=2^(nextpow2(N));   % transform length to power of 2 for optimal speed

x=detrend(w.*x);        % remove linear fit from data and apply window 
X=fft(x,nfft);          % FFT pads with zero's to get nfft length
Pxx=(abs(X).^2)*dz/2/pi/N;   % calculate power spectral density
m=nfft/2; 
Pxx(m+2:nfft)=[];       % throw away the redundant second half of spectrum 
Pxx(2:m+1)=2*Pxx(2:m+1);% multiply by factor 2 to compensate for 
%   wavenumbers that were thrown away (except for the constant component 
%   and Nyquist component)

kc=pi/dz;               % critical/max wavenumber (nyquist)
kz=kc*[0:m]'/m;% wavenumber bins
