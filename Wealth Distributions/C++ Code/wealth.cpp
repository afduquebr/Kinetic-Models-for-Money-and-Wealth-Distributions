#include<iostream>
#include<cmath>
#include<numeric>
#include <vector>
#include "Random64.h"
#include <algorithm>
#define _USE_MATH_DEFINES_

const int N = 10000; // Tamaño del sistema
const double Alpha = 1.0;// cantidad de dinero por persona
const double Beta = 1.0;// cantidad de bienes por persona
const double omega = 1.0; // Total de riqueza


class System{
private:
    std::vector<double> a,b,w,mw; //dinero, bienes, riqueza
    double P = 0.0; // precio
public:
    void Iniciar(void);
    void UnPaso(Crandom & ran64);
    double GetPrecio(void){return P;};
    double GetEntropy(int Nbins);
    double GetTotalW(void);
    std::vector<double> GetMW(void){return mw;};
    std::vector<double> GetW(void){return w;};
    std::vector<double> GetMoney(void){return a;};
    std::vector<double> GetGoods(void){return b;};
};

void Histogram (int N, int Nbins, std::vector<double> w);
void PrintVector(std::vector<double> vector);

int main(void){
    const int tmax = 20*N;// ciclos máximos de evolución 
    const int nprom = 5;
    std::vector<double> mw(N,0.0); //Vector de riqueza-money
    std::vector<double> a(N,0.0); //Vector de dinero
    std::vector<double> b(N,0.0); //Vector de bienes
    std::vector<double> WT(tmax,0.0); //Total wealth in term of money 
    std::vector<double> P(tmax,0.0); //Price in term of money 
    std::vector<double> S(tmax,0.0); //Entropy
    const int Nbins = 20; // Número de bins para el histograma y entropía
    Crandom ran64(1); // Generador aleatorio
    System Market; //Creamos el mercado


   for(int i = 0; i <nprom;i++){
        Market.Iniciar(); //inicializando el mercado
        for(int t = 0; t<tmax;t++){
            Market.UnPaso(ran64);
            //WT[t] += Market.GetTotalW();
            //P[t] += Market.GetPrecio();
            S[t] += Market.GetEntropy(Nbins);
        }
    }
    
    for(int t = 0; t < tmax;t++){
        std::cout<< t << "\t" /*<< (double)WT[t]/(N*nprom) << "\t"<< (double) P[t]/nprom << "\t"*/<< (double) S[t]/nprom<< std::endl;
    }

    /*for(int t = 0; t < tmax;t++){
        Market.UnPaso(ran64);
    }

    std::vector<double> aux (N,0.0);
    for (int i = 0; i < nprom;i++){
        aux = Market.GetMW();
        for(int j = 1; j < N;j++){
            a[j] += aux[j]/nprom;
        }
    }    
    Histogram(N, Nbins, a);
    //PrintVector(a);*/
    return 0;
}

void PrintVector(std::vector<double> vector){
    const int size = vector.size();
    for (int i =0; i < size;i++) {
        std::cout << vector[i] << std::endl;
    }
}

void Histogram (int N,int Nbins, std::vector<double> waux){
    std::sort(waux.begin(), waux.end()); //Ordenando el vector de mayor a menor
    double wmax = waux.back(); // Máxima riqueza obtenida
    const double dw = wmax/Nbins;
    for(int n = 0; n< Nbins;n++){
        int count = 0;
        for(int i = 0; i< N; i++){
            if((n+1.0)*dw >= waux[i] && waux[i] > n*dw)  count += 1; 
        }
        std::cout << (2.0*n +1.0)*dw/2.0 << "\t" << (double) count/N << std::endl;
    }
}

    double System::GetEntropy(int Nbins){
        double S = 0.0;
        std::sort(mw.begin(), mw.end()); //Ordenando el vector de mayor a menor
        double wmax = mw.back(); // Máxima riqueza obtenida
        const double dw = wmax/Nbins;
        std::vector<double>count(Nbins,0.0);
        for(int n = 0; n< Nbins;n++){
            for(int i = 0; i< N; i++){
                if((n+1.0)*dw >= mw[i] && mw[i] > n*dw)  count[n] += 1.0; 
            }
        }
        for(int n = 0;n <Nbins;n++){
            count[n] /=N;
            if (count[n] > 0.0 ) S+= -count[n]*std::log2(count[n])*dw;
        }
        return S;
    }

void System::Iniciar(void){
    a.resize(N,Alpha);
    b.resize(N,Beta);
    w.resize(N,0.0);
    mw.resize(N,0.0);
    P = 0.0;
    for(int i = 0; i < N;i++){
        a[i] = Alpha;
        b[i]=Beta;
        mw[i]=w[i]=0.0;
    }
}

    double System::GetTotalW(void){
        double WT = 0.0;
        WT = std::accumulate(w.begin(),w.end(),0.0);
        return WT;
    }
    
void System::UnPaso(Crandom & ran64){
    double p = 0.0;// Variables auxiliares
    double q = 0.0;// Variables auxiliares
    std::vector<double> f(N); //Parámetro de preferencia
    for(int i=0;i<N;i++) {
        f[i] = ran64.r();
    }
        
    for(int i = 0;i<N;i++){
        p += (1.0-f[i])*a[i];
        q += (f[i])*b[i];
    }
    P = p/q; //Precio
    //Caculando riqueza
    for (int i = 0; i <N;i++){
        w[i] = a[i] + P*b[i];
    }
    //Evolución del sistema
    for(int i =0;i<N;i++){
        a[i] = f[i]*w[i];
        b[i] = (1-f[i])*w[i]/P;
        mw[i] = omega*w[i]/(Alpha+Beta*P);
    }
}